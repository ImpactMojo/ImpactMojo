#!/usr/bin/env python3
"""
notebooklm-manage.py — Manage ImpactMojo NotebookLM study companions.

Programmatic access to the 11 AI Study Companion notebooks linked from
flagship course pages. Uses notebooklm-py (unofficial Google NotebookLM API).

Usage:
  python3 scripts/notebooklm-manage.py status
  python3 scripts/notebooklm-manage.py list
  python3 scripts/notebooklm-manage.py sync-registry
  python3 scripts/notebooklm-manage.py add-source <slug> <url-or-file>
  python3 scripts/notebooklm-manage.py generate-audio <slug>

Prerequisites:
  pip install -r requirements.txt && playwright install chromium
  notebooklm login   # one-time Google OAuth
"""

import asyncio, json, os, sys

# ─── Config ─────────────────────────────────────────────────────────────────

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(SCRIPT_DIR, "..")
REGISTRY_PATH = os.path.join(ROOT_DIR, "data", "notebooklm-registry.json")


# ─── Registry helpers ────────────────────────────────────────────────────────

def load_registry():
    """Load the notebook registry from data/notebooklm-registry.json."""
    with open(REGISTRY_PATH, "r") as f:
        return json.load(f)


def save_registry(data):
    """Write the notebook registry back to disk."""
    with open(REGISTRY_PATH, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


def get_notebook_id(slug):
    """Look up a notebook ID by course slug. Exits on unknown slug."""
    registry = load_registry()
    entry = registry["notebooks"].get(slug)
    if not entry:
        slugs = ", ".join(sorted(registry["notebooks"].keys()))
        print(f"Error: unknown course slug '{slug}'")
        print(f"Available: {slugs}")
        sys.exit(1)
    return entry["id"]


# ─── Commands ────────────────────────────────────────────────────────────────

async def cmd_status():
    """Check authentication status."""
    from notebooklm import NotebookLMClient
    try:
        async with NotebookLMClient.from_storage() as client:
            notebooks = await client.notebooks.list()
            print(f"Authenticated. {len(notebooks)} notebooks accessible.")
    except Exception as e:
        print(f"Not authenticated: {e}")
        print("Run: notebooklm login")
        sys.exit(1)


async def cmd_list():
    """List all notebooks, cross-referenced with the registry."""
    from notebooklm import NotebookLMClient

    registry = load_registry()
    registered_ids = {v["id"]: k for k, v in registry["notebooks"].items()}

    async with NotebookLMClient.from_storage() as client:
        notebooks = await client.notebooks.list()

        print(f"{'Slug':<12} {'Title':<45} {'Sources':>7}")
        print("─" * 66)
        for nb in notebooks:
            nb_id = nb.id if hasattr(nb, "id") else str(nb)
            title = nb.title if hasattr(nb, "title") else "—"
            sources = nb.source_count if hasattr(nb, "source_count") else "?"
            slug = registered_ids.get(nb_id, "—")
            print(f"{slug:<12} {title:<45} {sources:>7}")

        # Show registered notebooks not found in the API response
        api_ids = {nb.id if hasattr(nb, "id") else str(nb) for nb in notebooks}
        missing = [s for s, v in registry["notebooks"].items() if v["id"] not in api_ids]
        if missing:
            print(f"\nNot found in API (may need sharing): {', '.join(missing)}")


async def cmd_sync_registry():
    """Sync registry with live notebook data from the API."""
    from notebooklm import NotebookLMClient

    registry = load_registry()

    async with NotebookLMClient.from_storage() as client:
        notebooks = await client.notebooks.list()
        api_map = {}
        for nb in notebooks:
            nb_id = nb.id if hasattr(nb, "id") else str(nb)
            api_map[nb_id] = nb

        updated = 0
        for slug, entry in registry["notebooks"].items():
            nb = api_map.get(entry["id"])
            if nb and hasattr(nb, "title"):
                old_title = entry.get("title", "")
                new_title = nb.title
                if old_title != new_title:
                    entry["title"] = new_title
                    updated += 1
                    print(f"  Updated {slug}: {old_title!r} -> {new_title!r}")

    if updated:
        save_registry(registry)
        print(f"\nSynced {updated} notebook(s) to {REGISTRY_PATH}")
    else:
        print("Registry already up to date.")


async def cmd_add_source(slug, source_path):
    """Add a URL or file as a source to a course notebook."""
    from notebooklm import NotebookLMClient

    notebook_id = get_notebook_id(slug)

    async with NotebookLMClient.from_storage() as client:
        if source_path.startswith("http://") or source_path.startswith("https://"):
            result = await client.sources.add_url(notebook_id, source_path)
            print(f"Added URL source to {slug}: {source_path}")
        elif os.path.isfile(source_path):
            result = await client.sources.add_file(notebook_id, source_path)
            print(f"Added file source to {slug}: {source_path}")
        else:
            print(f"Error: '{source_path}' is not a valid URL or existing file.")
            sys.exit(1)


async def cmd_generate_audio(slug):
    """Generate an audio overview for a course notebook."""
    from notebooklm import NotebookLMClient

    notebook_id = get_notebook_id(slug)

    async with NotebookLMClient.from_storage() as client:
        print(f"Generating audio for {slug}... (this may take a few minutes)")
        result = await client.artifacts.generate_audio(notebook_id)
        print(f"Audio generated for {slug}.")
        if hasattr(result, "url"):
            print(f"URL: {result.url}")
        elif hasattr(result, "download_url"):
            print(f"Download: {result.download_url}")
        else:
            print(f"Result: {result}")


# ─── Main ────────────────────────────────────────────────────────────────────

COMMANDS = {
    "status": (cmd_status, 0),
    "list": (cmd_list, 0),
    "sync-registry": (cmd_sync_registry, 0),
    "add-source": (cmd_add_source, 2),
    "generate-audio": (cmd_generate_audio, 1),
}


def usage():
    print(__doc__.strip())
    print(f"\nCommands: {', '.join(COMMANDS.keys())}")
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        usage()

    cmd = sys.argv[1]
    if cmd in ("-h", "--help", "help"):
        usage()

    if cmd not in COMMANDS:
        print(f"Unknown command: {cmd}")
        usage()

    func, nargs = COMMANDS[cmd]
    args = sys.argv[2:]
    if len(args) < nargs:
        print(f"Error: '{cmd}' requires {nargs} argument(s), got {len(args)}")
        usage()

    asyncio.run(func(*args[:nargs]))


if __name__ == "__main__":
    main()
