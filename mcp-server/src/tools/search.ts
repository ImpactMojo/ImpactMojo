import { z } from "zod";
import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import type { LoadedData, SearchEntry } from "../data-loader.js";

function matchesQuery(entry: SearchEntry, tokens: string[]): boolean {
  const haystack = `${entry.title} ${entry.description} ${entry.tags.join(" ")}`.toLowerCase();
  return tokens.every((t) => haystack.includes(t));
}

function relevanceScore(entry: SearchEntry, tokens: string[]): number {
  const titleLower = entry.title.toLowerCase();
  let score = 0;
  for (const t of tokens) {
    if (titleLower.includes(t)) score += 2;
  }
  return score;
}

export function registerSearchTools(server: McpServer, data: LoadedData) {
  server.tool(
    "search_content",
    "Search across all ImpactMojo content — courses, games, labs, BCTs, dataverse tools, handouts, book summaries, and more. Returns matching items with titles, descriptions, and URLs.",
    {
      query: z.string().describe("Search term (e.g. 'gender equity', 'logframe', 'climate')"),
      type: z.string().optional().describe("Filter by content type: bct, course, game, lab, dataverse, book-summary, page, tool, devdiscourse"),
      category: z.string().optional().describe("Filter by category name"),
      tag: z.string().optional().describe("Filter by tag"),
      limit: z.number().optional().default(10).describe("Max results (default 10, max 50)"),
    },
    async ({ query, type, category, tag, limit }) => {
      const tokens = query.toLowerCase().split(/\s+/).filter(Boolean);
      const cap = Math.min(limit ?? 10, 50);

      let results = data.searchIndex.filter((entry) => {
        if (!matchesQuery(entry, tokens)) return false;
        if (type && entry.type !== type) return false;
        if (category && !entry.category.toLowerCase().includes(category.toLowerCase())) return false;
        if (tag && !entry.tags.some((t) => t.toLowerCase().includes(tag.toLowerCase()))) return false;
        return true;
      });

      results.sort((a, b) => relevanceScore(b, tokens) - relevanceScore(a, tokens));
      results = results.slice(0, cap);

      if (results.length === 0) {
        return { content: [{ type: "text" as const, text: `No results found for "${query}".` }] };
      }

      const output = results.map((r) => ({
        id: r.id,
        title: r.title,
        type: r.type,
        category: r.category,
        url: `https://impactmojo.in${r.url}`,
        description: r.description.slice(0, 200),
        tags: r.tags,
      }));

      return {
        content: [{
          type: "text" as const,
          text: `Found ${results.length} result(s) for "${query}":\n\n${JSON.stringify(output, null, 2)}`,
        }],
      };
    }
  );
}
