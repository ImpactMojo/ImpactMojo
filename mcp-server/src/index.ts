#!/usr/bin/env node

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { loadAllData } from "./data-loader.js";
import { registerSearchTools } from "./tools/search.js";
import { registerBCTTools } from "./tools/bct.js";
import { registerDataverseTools } from "./tools/dataverse.js";
import { registerChallengeTools } from "./tools/challenges.js";
import { registerCourseTools } from "./tools/courses.js";
import { registerGamesLabsTools } from "./tools/games-labs.js";
import { registerClimateTools } from "./tools/climate.js";
import { registerResources } from "./resources/platform.js";

// Load all data from JSON files at startup
const data = loadAllData();

const server = new McpServer({
  name: "impactmojo",
  version: "1.0.0",
});

// Register all tools
registerSearchTools(server, data);
registerBCTTools(server, data);
registerDataverseTools(server, data);
registerChallengeTools(server, data);
registerCourseTools(server, data);
registerGamesLabsTools(server, data);
registerClimateTools(server, data);

// Register resources
registerResources(server, data);

// Connect via stdio transport
const transport = new StdioServerTransport();
await server.connect(transport);
