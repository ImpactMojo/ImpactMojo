// Copy data files from repo root into mcp-server/data/ for npm packaging
import { cpSync, mkdirSync, existsSync } from "fs";
import { resolve, dirname } from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const repoData = resolve(__dirname, "../../data");
const localData = resolve(__dirname, "../data");
const catalogSrc = resolve(__dirname, "../../catalog_data.json");
const catalogDst = resolve(localData, "catalog_data.json");

const files = [
  "search-index.json",
  "bct-repository.json",
  "dataverse.json",
  "challenges.json",
  "game-agents.json",
  "climate-trace-india.json",
];

mkdirSync(localData, { recursive: true });

for (const f of files) {
  const src = resolve(repoData, f);
  const dst = resolve(localData, f);
  if (existsSync(src)) {
    cpSync(src, dst);
    console.log(`  Copied ${f}`);
  } else {
    console.warn(`  Warning: ${src} not found`);
  }
}

if (existsSync(catalogSrc)) {
  cpSync(catalogSrc, catalogDst);
  console.log("  Copied catalog_data.json");
}

console.log("Data files copied for packaging.");
