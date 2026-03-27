import { readFileSync } from "fs";
import { resolve, dirname } from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Resolve paths relative to the repo root (mcp-server/dist/ -> repo root)
function dataPath(filename: string): string {
  return resolve(__dirname, "../../data", filename);
}

function rootPath(filename: string): string {
  return resolve(__dirname, "../..", filename);
}

// --- Type definitions ---

export interface SearchEntry {
  id: string;
  title: string;
  description: string;
  type: string;
  category: string;
  url: string;
  tags: string[];
}

export interface BCTCaseStudy {
  title: string;
  sector: string;
  country: string;
  description: string;
  outcome: string;
  source: string;
}

export interface BCTTechnique {
  id: string;
  name: string;
  definition: string;
  example: string;
  southAsianContext: string;
  sectors: string[];
  evidenceLevel: string;
  implementationTips: string[];
  relatedTechniques: string[];
  caseStudies: BCTCaseStudy[];
  categoryId: string;
  categoryName: string;
}

export interface BCTCategory {
  id: string;
  name: string;
  description: string;
  techniqueCount: number;
}

export interface DataverseItem {
  id: string;
  name: string;
  description: string;
  type: string;
  status: string;
  url: string;
  source: string;
  tags: string[];
  free: boolean;
  categoryId: string;
  categoryName: string;
}

export interface DataverseCategory {
  id: string;
  name: string;
  icon: string;
  description: string;
  itemCount: number;
}

export interface Challenge {
  id: string;
  title: string;
  track: string;
  trackLabel: string;
  courseId: string;
  difficulty: string;
  requiredTier: string;
  durationMinutes: number;
  submissions: number;
  status: string;
  description: string;
  caseContext: string;
  learningOutcomes: string[];
  submissionTemplate: string;
  rubric: { criterion: string; weight: number }[];
  resources: { label: string; url: string }[];
}

export interface Course {
  title: string;
  type: string;
  track: string;
  level: string;
  link: string;
}

export interface GameAgent {
  id: string;
  name: string;
  role: string;
  location: string;
  personality: {
    archetype: string;
    cooperation_bias: number;
    risk_tolerance: number;
    memory_weight: number;
    description: string;
  };
  backstory: string;
  strategy_hint: string;
}

export interface Game {
  name: string;
  concept: string;
  roundCount: number;
  agents: GameAgent[];
}

export interface ClimateYearData {
  status: string;
  note?: string;
  overview: Record<string, number>;
  sectors: Record<string, Record<string, unknown>>;
  subsectors_2022?: Record<string, unknown>;
  top_power_plants?: unknown[];
}

export interface ClimateData {
  source: string;
  api: string;
  country: string;
  global_rank: number;
  primary_year: number;
  retrieved: string;
  years: Record<string, ClimateYearData>;
}

export interface LoadedData {
  searchIndex: SearchEntry[];
  bctTechniques: Map<string, BCTTechnique>;
  bctCategories: BCTCategory[];
  dataverseItems: DataverseItem[];
  dataverseCategories: DataverseCategory[];
  challenges: Challenge[];
  courses: Course[];
  games: Map<string, Game>;
  climateData: ClimateData;
}

function loadJSON(filepath: string): unknown {
  const raw = readFileSync(filepath, "utf-8");
  return JSON.parse(raw);
}

export function loadAllData(): LoadedData {
  // 1. Search index
  const searchIndex = loadJSON(dataPath("search-index.json")) as SearchEntry[];

  // 2. BCT repository — flatten techniques from nested categories
  const bctRaw = loadJSON(dataPath("bct-repository.json")) as {
    categories: {
      id: string;
      name: string;
      description: string;
      techniques: Omit<BCTTechnique, "categoryId" | "categoryName">[];
    }[];
  };

  const bctTechniques = new Map<string, BCTTechnique>();
  const bctCategories: BCTCategory[] = [];

  for (const cat of bctRaw.categories) {
    bctCategories.push({
      id: cat.id,
      name: cat.name,
      description: cat.description,
      techniqueCount: cat.techniques.length,
    });
    for (const tech of cat.techniques) {
      bctTechniques.set(tech.id, {
        ...tech,
        categoryId: cat.id,
        categoryName: cat.name,
      });
    }
  }

  // 3. Dataverse — flatten items from nested categories
  const dvRaw = loadJSON(dataPath("dataverse.json")) as {
    meta: Record<string, unknown>;
    categories: {
      id: string;
      name: string;
      icon: string;
      description: string;
      items: Omit<DataverseItem, "categoryId" | "categoryName">[];
    }[];
  };

  const dataverseItems: DataverseItem[] = [];
  const dataverseCategories: DataverseCategory[] = [];

  for (const cat of dvRaw.categories) {
    dataverseCategories.push({
      id: cat.id,
      name: cat.name,
      icon: cat.icon,
      description: cat.description,
      itemCount: cat.items.length,
    });
    for (const item of cat.items) {
      dataverseItems.push({
        ...item,
        categoryId: cat.id,
        categoryName: cat.name,
      });
    }
  }

  // 4. Challenges
  const challenges = loadJSON(dataPath("challenges.json")) as Challenge[];

  // 5. Courses from catalog_data.json
  const catalogRaw = loadJSON(rootPath("catalog_data.json")) as {
    DATA: Course[];
  };
  const courses = catalogRaw.DATA;

  // 6. Games
  const gamesRaw = loadJSON(dataPath("game-agents.json")) as {
    games: Record<string, Game>;
  };
  const games = new Map<string, Game>();
  for (const [key, game] of Object.entries(gamesRaw.games)) {
    games.set(key, game);
  }

  // 7. Climate data
  const climateData = loadJSON(dataPath("climate-trace-india.json")) as ClimateData;

  return {
    searchIndex,
    bctTechniques,
    bctCategories,
    dataverseItems,
    dataverseCategories,
    challenges,
    courses,
    games,
    climateData,
  };
}
