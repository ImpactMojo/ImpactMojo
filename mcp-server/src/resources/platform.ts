import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import type { LoadedData } from "../data-loader.js";

export function registerResources(server: McpServer, data: LoadedData) {
  server.resource(
    "platform-overview",
    "impactmojo://overview",
    {
      description: "ImpactMojo platform overview — what it is, who it serves, and what content is available",
      mimeType: "text/markdown",
    },
    async () => {
      const gameCount = data.games.size;
      const courseCount = data.courses.length;
      const bctCount = data.bctTechniques.size;
      const dvCount = data.dataverseItems.length;
      const challengeCount = data.challenges.length;
      const searchCount = data.searchIndex.length;

      return {
        contents: [{
          uri: "impactmojo://overview",
          mimeType: "text/markdown",
          text: `# ImpactMojo

**Free development education platform for South Asia**
Website: https://impactmojo.in

## What is ImpactMojo?

ImpactMojo is a free, open-access education platform focused on development economics, monitoring & evaluation, policy analysis, and social impact — with a South Asian lens. It serves development practitioners, students, researchers, and NGO professionals across India and the region.

## Content at a Glance

| Content Type | Count | Description |
|---|---|---|
| Courses | ${courseCount} | 9 flagship + ${courseCount - 9} foundational courses |
| Games | ${gameCount} | Economics simulation games with AI agents |
| Labs | 8 | Browser-based interactive workbenches |
| BCT Techniques | ${bctCount} | Behavior Change Techniques with South Asian context |
| Dataverse | ${dvCount} | Tools, datasets, APIs, and MCP servers |
| Challenges | ${challengeCount} | Practice exercises with rubrics |
| Handouts | 400+ | Downloadable resources across 12 tracks |
| Book Summaries | 30 | Companion guides for canonical texts |
| Total Indexed Items | ${searchCount} | Searchable via search_content tool |

## Learning Tracks

1. **Monitoring, Evaluation & Learning** — Logframes, theory of change, impact evaluation
2. **Data & Technology** — Data visualization, AI for development, digital tools
3. **Policy & Economics** — Development economics, public policy, governance
4. **Philosophy, Law & Governance** — Gandhi, constitutional law, ethics
5. **Health & Communication** — Public health, behavior change, media
6. **Gender & Equity** — Gender studies, social inclusion, intersectionality

## Technology

Static HTML/CSS/JS site hosted on Netlify, with Supabase backend for game AI agents and user progress. All content is freely accessible without login.
`,
        }],
      };
    }
  );

  server.resource(
    "content-catalog",
    "impactmojo://catalog",
    {
      description: "Complete content catalog — all courses with tracks and levels",
      mimeType: "text/markdown",
    },
    async () => {
      // Group courses by track
      const byTrack = new Map<string, typeof data.courses>();
      for (const course of data.courses) {
        const list = byTrack.get(course.track) ?? [];
        list.push(course);
        byTrack.set(course.track, list);
      }

      let md = "# ImpactMojo Content Catalog\n\n";

      // Courses by track
      md += "## Courses\n\n";
      for (const [track, courses] of byTrack) {
        md += `### ${track}\n\n`;
        md += "| Course | Type | Level |\n|---|---|---|\n";
        for (const c of courses) {
          md += `| ${c.title} | ${c.type} | ${c.level} |\n`;
        }
        md += "\n";
      }

      // Games
      md += "## Economics Simulation Games\n\n";
      md += "| Game | Concept | Rounds | AI Agents |\n|---|---|---|---|\n";
      for (const [id, game] of data.games) {
        md += `| ${game.name} | ${game.concept} | ${game.roundCount} | ${game.agents.length} |\n`;
      }
      md += "\n";

      // Challenges
      md += "## Practice Challenges\n\n";
      md += "| Challenge | Track | Difficulty | Duration |\n|---|---|---|---|\n";
      for (const c of data.challenges) {
        md += `| ${c.title} | ${c.trackLabel} | ${c.difficulty} | ${c.durationMinutes}min |\n`;
      }

      return {
        contents: [{
          uri: "impactmojo://catalog",
          mimeType: "text/markdown",
          text: md,
        }],
      };
    }
  );

  server.resource(
    "learning-tracks",
    "impactmojo://tracks",
    {
      description: "Learning tracks overview with course counts and descriptions",
      mimeType: "text/markdown",
    },
    async () => {
      const trackCounts = new Map<string, number>();
      for (const c of data.courses) {
        trackCounts.set(c.track, (trackCounts.get(c.track) ?? 0) + 1);
      }

      let md = "# ImpactMojo Learning Tracks\n\n";

      const tracks = [
        { name: "Monitoring, Evaluation & Learning", desc: "Master the MEL cycle — logframes, theory of change, indicator design, impact evaluation, and adaptive management. The backbone of evidence-based development practice." },
        { name: "Data & Technology", desc: "Data visualization, AI for development, digital public infrastructure, and computational tools for social impact measurement." },
        { name: "Policy & Economics", desc: "Development economics, public policy analysis, governance frameworks, and the political economy of reform in South Asia." },
        { name: "Philosophy, Law & Governance", desc: "Gandhian thought, constitutional law, ethics of development, governance institutions, and justice frameworks." },
        { name: "Health & Communication", desc: "Public health systems, behavior change communication, media for development, and health economics." },
        { name: "Gender & Equity", desc: "Gender analysis, intersectionality, social inclusion, women's empowerment, and equity-focused programming." },
      ];

      for (const t of tracks) {
        const count = trackCounts.get(t.name) ?? 0;
        md += `## ${t.name} (${count} courses)\n\n${t.desc}\n\n`;
      }

      return {
        contents: [{
          uri: "impactmojo://tracks",
          mimeType: "text/markdown",
          text: md,
        }],
      };
    }
  );
}
