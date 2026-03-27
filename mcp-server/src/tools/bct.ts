import { z } from "zod";
import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import type { LoadedData, BCTTechnique } from "../data-loader.js";

export function registerBCTTools(server: McpServer, data: LoadedData) {
  server.tool(
    "lookup_bct",
    "Get full details of a specific Behavior Change Technique by ID, including definition, South Asian context, implementation tips, and case studies.",
    {
      id: z.string().describe("BCT ID, e.g. 'BCT001', 'BCT045', 'BCT180'"),
    },
    async ({ id }) => {
      const normalized = id.toUpperCase();
      const tech = data.bctTechniques.get(normalized);
      if (!tech) {
        return { content: [{ type: "text" as const, text: `BCT "${id}" not found. Use list_bct_categories or search_bcts to discover available techniques.` }] };
      }
      return {
        content: [{
          type: "text" as const,
          text: JSON.stringify({
            id: tech.id,
            name: tech.name,
            category: tech.categoryName,
            definition: tech.definition,
            example: tech.example,
            southAsianContext: tech.southAsianContext,
            sectors: tech.sectors,
            evidenceLevel: tech.evidenceLevel,
            implementationTips: tech.implementationTips,
            relatedTechniques: tech.relatedTechniques,
            caseStudies: tech.caseStudies,
          }, null, 2),
        }],
      };
    }
  );

  server.tool(
    "search_bcts",
    "Search and filter 203 Behavior Change Techniques by keyword, sector, category, or evidence level. Returns compact results — use lookup_bct for full details.",
    {
      query: z.string().optional().describe("Keyword search across name, definition, and South Asian context"),
      sector: z.string().optional().describe("Filter by sector: Health, WASH, Education, Nutrition, Agriculture, Livelihoods, etc."),
      category: z.string().optional().describe("Filter by category name, e.g. 'Goals & Planning', 'Nudge & Choice Architecture'"),
      evidenceLevel: z.string().optional().describe("Filter by evidence level: Strong, Moderate, Emerging"),
      limit: z.number().optional().default(10).describe("Max results (default 10)"),
    },
    async ({ query, sector, category, evidenceLevel, limit }) => {
      if (!query && !sector && !category && !evidenceLevel) {
        return { content: [{ type: "text" as const, text: "Please provide at least one of: query, sector, category, or evidenceLevel." }] };
      }

      const tokens = query ? query.toLowerCase().split(/\s+/).filter(Boolean) : [];
      const cap = Math.min(limit ?? 10, 50);

      let results: BCTTechnique[] = [];
      for (const tech of data.bctTechniques.values()) {
        if (tokens.length > 0) {
          const haystack = `${tech.name} ${tech.definition} ${tech.southAsianContext}`.toLowerCase();
          if (!tokens.every((t) => haystack.includes(t))) continue;
        }
        if (sector && !tech.sectors.some((s) => s.toLowerCase().includes(sector.toLowerCase()))) continue;
        if (category && !tech.categoryName.toLowerCase().includes(category.toLowerCase())) continue;
        if (evidenceLevel && tech.evidenceLevel.toLowerCase() !== evidenceLevel.toLowerCase()) continue;
        results.push(tech);
      }

      results = results.slice(0, cap);

      if (results.length === 0) {
        return { content: [{ type: "text" as const, text: "No BCTs matched your criteria." }] };
      }

      const output = results.map((t) => ({
        id: t.id,
        name: t.name,
        category: t.categoryName,
        sectors: t.sectors,
        evidenceLevel: t.evidenceLevel,
        definition: t.definition.slice(0, 150),
      }));

      return {
        content: [{
          type: "text" as const,
          text: `Found ${results.length} BCT(s):\n\n${JSON.stringify(output, null, 2)}`,
        }],
      };
    }
  );

  server.tool(
    "list_bct_categories",
    "List all 26 Behavior Change Technique categories with technique counts. Use this to discover what's available before searching.",
    {},
    async () => {
      const output = data.bctCategories.map((c) => ({
        id: c.id,
        name: c.name,
        description: c.description,
        techniques: c.techniqueCount,
      }));

      return {
        content: [{
          type: "text" as const,
          text: `${data.bctCategories.length} BCT categories (${data.bctTechniques.size} total techniques):\n\n${JSON.stringify(output, null, 2)}`,
        }],
      };
    }
  );
}
