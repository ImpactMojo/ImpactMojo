import { z } from "zod";
import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import type { LoadedData } from "../data-loader.js";

export function registerCourseTools(server: McpServer, data: LoadedData) {
  server.tool(
    "list_courses",
    "List ImpactMojo courses — 9 flagship and 39 foundational courses across 6 learning tracks. Filter by track, type, or level.",
    {
      track: z.string().optional().describe("Filter by track name, e.g. 'Policy & Economics', 'Data & Technology'"),
      type: z.string().optional().describe("Filter by type: Flagship, Course"),
      level: z.string().optional().describe("Filter by level: Advanced, Core, Intro"),
    },
    async ({ track, type, level }) => {
      let results = data.courses;
      if (track) results = results.filter((c) => c.track.toLowerCase().includes(track.toLowerCase()));
      if (type) results = results.filter((c) => c.type === type);
      if (level) results = results.filter((c) => c.level === level);

      if (results.length === 0) {
        return { content: [{ type: "text" as const, text: "No courses match your criteria." }] };
      }

      const output = results.map((c) => ({
        title: c.title,
        type: c.type,
        track: c.track,
        level: c.level,
        url: c.link.startsWith("http") ? c.link : `https://impactmojo.in${c.link}`,
      }));

      // Group by track for readability
      const tracks = [...new Set(results.map((c) => c.track))];
      const summary = tracks.map((t) => `${t}: ${results.filter((c) => c.track === t).length}`).join(", ");

      return {
        content: [{
          type: "text" as const,
          text: `${results.length} course(s) [${summary}]:\n\n${JSON.stringify(output, null, 2)}`,
        }],
      };
    }
  );
}
