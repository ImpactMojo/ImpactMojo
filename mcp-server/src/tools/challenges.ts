import { z } from "zod";
import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import type { LoadedData } from "../data-loader.js";

export function registerChallengeTools(server: McpServer, data: LoadedData) {
  server.tool(
    "list_challenges",
    "List available practice challenges for development professionals. Filter by track or difficulty.",
    {
      track: z.string().optional().describe("Filter by track: mel, dataviz, devecon, gender, law, policy, devai"),
      difficulty: z.string().optional().describe("Filter by difficulty: beginner, intermediate, advanced"),
    },
    async ({ track, difficulty }) => {
      let results = data.challenges;
      if (track) results = results.filter((c) => c.track === track);
      if (difficulty) results = results.filter((c) => c.difficulty === difficulty);

      if (results.length === 0) {
        return { content: [{ type: "text" as const, text: "No challenges match your criteria." }] };
      }

      const output = results.map((c) => ({
        id: c.id,
        title: c.title,
        track: c.trackLabel,
        difficulty: c.difficulty,
        duration: `${c.durationMinutes} min`,
        description: c.description.slice(0, 120),
      }));

      return {
        content: [{
          type: "text" as const,
          text: `${results.length} challenge(s):\n\n${JSON.stringify(output, null, 2)}`,
        }],
      };
    }
  );

  server.tool(
    "get_challenge",
    "Get full details of a practice challenge including case context, learning outcomes, submission template, and rubric.",
    {
      id: z.string().describe("Challenge ID, e.g. 'mel-logframe-redesign'"),
    },
    async ({ id }) => {
      const challenge = data.challenges.find((c) => c.id === id);
      if (!challenge) {
        return { content: [{ type: "text" as const, text: `Challenge "${id}" not found. Use list_challenges to see available challenges.` }] };
      }

      return {
        content: [{
          type: "text" as const,
          text: JSON.stringify({
            id: challenge.id,
            title: challenge.title,
            track: challenge.trackLabel,
            difficulty: challenge.difficulty,
            duration: `${challenge.durationMinutes} min`,
            description: challenge.description,
            caseContext: challenge.caseContext,
            learningOutcomes: challenge.learningOutcomes,
            submissionTemplate: challenge.submissionTemplate,
            rubric: challenge.rubric,
            resources: challenge.resources,
          }, null, 2),
        }],
      };
    }
  );
}
