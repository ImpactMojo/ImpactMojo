import { z } from "zod";
import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import type { LoadedData } from "../data-loader.js";

export function registerGamesLabsTools(server: McpServer, data: LoadedData) {
  server.tool(
    "get_game_info",
    "Get details about ImpactMojo's 16 economics simulation games, including AI agent personas with South Asian backstories. Omit gameId to list all games.",
    {
      gameId: z.string().optional().describe("Game ID, e.g. 'public-good-game', 'tragedy-of-commons'. Omit to list all games."),
    },
    async ({ gameId }) => {
      if (!gameId) {
        // List all games
        const games: { id: string; name: string; concept: string; rounds: number; agents: number }[] = [];
        for (const [id, game] of data.games) {
          games.push({
            id,
            name: game.name,
            concept: game.concept,
            rounds: game.roundCount,
            agents: game.agents.length,
          });
        }
        return {
          content: [{
            type: "text" as const,
            text: `${games.length} economics simulation games:\n\n${JSON.stringify(games, null, 2)}`,
          }],
        };
      }

      const game = data.games.get(gameId);
      if (!game) {
        return { content: [{ type: "text" as const, text: `Game "${gameId}" not found. Call without gameId to list all games.` }] };
      }

      const output = {
        id: gameId,
        name: game.name,
        concept: game.concept,
        rounds: game.roundCount,
        agents: game.agents.map((a) => ({
          id: a.id,
          name: a.name,
          role: a.role,
          location: a.location,
          archetype: a.personality.archetype,
          backstory: a.backstory,
          cooperationBias: a.personality.cooperation_bias,
          riskTolerance: a.personality.risk_tolerance,
        })),
        url: `https://impactmojo.in/Games/${gameId}.html`,
      };

      return {
        content: [{
          type: "text" as const,
          text: JSON.stringify(output, null, 2),
        }],
      };
    }
  );
}
