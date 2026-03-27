import { z } from "zod";
import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import type { LoadedData } from "../data-loader.js";

export function registerClimateTools(server: McpServer, data: LoadedData) {
  server.tool(
    "query_climate_data",
    "Query India's greenhouse gas emissions data from Climate TRACE. Covers 10 sectors, 2024-2025 data. India is the world's 3rd largest emitter.",
    {
      year: z.string().optional().default("2024").describe("Year: '2024' (full data) or '2025' (preliminary)"),
      sector: z.string().optional().describe("Specific sector: power, agriculture, manufacturing, buildings, transportation, waste, forestry_and_land_use, fossil_fuel_operations, fluorinated_gases, mineral_extraction"),
      info: z.enum(["overview", "sectors", "all"]).optional().default("overview").describe("What to return: 'overview' (totals), 'sectors' (all sectors), 'all' (everything)"),
    },
    async ({ year, sector, info }) => {
      const yearKey = year ?? "2024";
      const yearData = data.climateData.years[yearKey];

      if (!yearData) {
        const available = Object.keys(data.climateData.years).join(", ");
        return { content: [{ type: "text" as const, text: `No data for year "${yearKey}". Available years: ${available}` }] };
      }

      // Specific sector query
      if (sector) {
        const sectorData = yearData.sectors[sector];
        if (!sectorData) {
          const available = Object.keys(yearData.sectors).join(", ");
          return { content: [{ type: "text" as const, text: `Sector "${sector}" not found. Available sectors: ${available}` }] };
        }
        return {
          content: [{
            type: "text" as const,
            text: JSON.stringify({
              country: data.climateData.country,
              globalRank: data.climateData.global_rank,
              year: yearKey,
              status: yearData.status,
              sector,
              data: sectorData,
            }, null, 2),
          }],
        };
      }

      // Overview or all sectors
      const result: Record<string, unknown> = {
        source: data.climateData.source,
        country: data.climateData.country,
        globalRank: data.climateData.global_rank,
        year: yearKey,
        status: yearData.status,
        overview: yearData.overview,
      };

      if (info === "sectors" || info === "all") {
        result.sectors = yearData.sectors;
      }

      return {
        content: [{
          type: "text" as const,
          text: JSON.stringify(result, null, 2),
        }],
      };
    }
  );
}
