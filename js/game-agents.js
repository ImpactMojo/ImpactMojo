/**
 * ImpactMojo Game Agents Client
 * Version: 1.0.0
 * Date: March 17, 2026
 *
 * MiroFish-inspired client library for AI-powered game opponents.
 * Provides the bridge between game frontends (101.impactmojo.in)
 * and the game-agent Supabase Edge Function.
 *
 * USAGE (in any game HTML):
 *   <script src="https://www.impactmojo.in/js/game-agents.js"></script>
 *
 *   // Initialise for a specific game
 *   var agents = new IMGameAgents('public-good-game');
 *
 *   // Get a single agent's decision
 *   agents.getDecision('pg-altruist', {
 *     round: 3,
 *     totalRounds: 10,
 *     history: [...],
 *     availableActions: ['contribute'],
 *     context: { max_contribution: 100 }
 *   }).then(function(decision) {
 *     console.log(decision.action, decision.amount, decision.reasoning);
 *   });
 *
 *   // Get ALL agents' decisions for a round (parallel)
 *   agents.getAllDecisions({
 *     round: 3,
 *     totalRounds: 10,
 *     history: [...],
 *     availableActions: ['cooperate', 'defect']
 *   }).then(function(decisions) {
 *     // decisions is { 'pg-altruist': {...}, 'pg-freerider': {...}, ... }
 *   });
 *
 *   // Get agent roster (names, roles, personalities) for UI display
 *   agents.getRoster().then(function(roster) {
 *     roster.forEach(function(a) {
 *       console.log(a.name, a.role, a.personality.archetype);
 *     });
 *   });
 */

(function () {
  'use strict';

  // ── Configuration ──────────────────────────────────────────────────

  var CONFIG = {
    // Supabase Edge Function endpoint
    EDGE_FUNCTION_URL: 'https://ddyszmfffyedolkcugld.supabase.co/functions/v1/game-agent',

    // Fallback: load agent data directly for offline/free-tier play
    AGENT_DATA_URL: 'https://www.impactmojo.in/data/game-agents.json',

    // Request timeout (ms)
    TIMEOUT: 8000,

    // Retry config
    MAX_RETRIES: 2,
    RETRY_DELAY: 1000
  };

  // ── Agent data cache ───────────────────────────────────────────────

  var _agentDataCache = null;
  var _agentDataPromise = null;

  function loadAgentData() {
    if (_agentDataCache) return Promise.resolve(_agentDataCache);
    if (_agentDataPromise) return _agentDataPromise;

    _agentDataPromise = fetch(CONFIG.AGENT_DATA_URL)
      .then(function (resp) {
        if (!resp.ok) throw new Error('Failed to load agent data');
        return resp.json();
      })
      .then(function (data) {
        _agentDataCache = data;
        return data;
      })
      .catch(function (err) {
        console.warn('[IMGameAgents] Could not load agent data:', err);
        _agentDataPromise = null;
        return null;
      });

    return _agentDataPromise;
  }

  // ── Local fallback engine ──────────────────────────────────────────
  // Mirrors the Edge Function's fallback logic for offline/free-tier use.

  function localDecision(agent, opts) {
    var p = agent.personality;
    var actions = opts.availableActions;
    var history = opts.history || [];
    var round = opts.round;
    var totalRounds = opts.totalRounds;
    var ctx = opts.context || {};

    // Binary games (cooperate/defect)
    if (actions.indexOf('cooperate') !== -1 && actions.indexOf('defect') !== -1) {
      var cooperateProb = p.cooperation_bias;

      if (history.length > 0 && p.memory_weight > 0) {
        var lastRound = history[history.length - 1];
        if (lastRound.player_action === 'defect') {
          cooperateProb -= 0.3 * p.memory_weight;
        }
      }

      if (round > totalRounds * 0.8) {
        cooperateProb -= 0.15 * p.risk_tolerance;
      }

      cooperateProb = Math.max(0.05, Math.min(0.95, cooperateProb));
      var action = Math.random() < cooperateProb ? 'cooperate' : 'defect';

      return {
        action: action,
        amount: null,
        reasoning: agent.name + ' ' + (action === 'cooperate'
          ? 'decides to cooperate — ' + p.archetype + ' instincts.'
          : 'defects — ' + p.archetype + ' calculus.'),
        agent_id: agent.id,
        agent_name: agent.name,
        personality: p.archetype
      };
    }

    // Contribution games
    if (actions.indexOf('contribute') !== -1) {
      var maxC = ctx.max_contribution || 100;
      var base = maxC * p.cooperation_bias;

      if (history.length > 0 && p.memory_weight > 0) {
        var last = history[history.length - 1];
        var contribs = [];
        if (last.agent_actions) {
          var keys = Object.keys(last.agent_actions);
          for (var k = 0; k < keys.length; k++) {
            contribs.push(last.agent_actions[keys[k]].amount || 0);
          }
        }
        if (contribs.length > 0) {
          var avg = contribs.reduce(function (s, v) { return s + v; }, 0) / contribs.length;
          var groupRatio = avg / maxC;
          base = base * (1 - p.memory_weight) + maxC * groupRatio * p.memory_weight;
        }
      }

      var noise = (Math.random() - 0.5) * maxC * 0.2 * p.risk_tolerance;
      var amount = Math.round(Math.max(0, Math.min(maxC, base + noise)));

      return {
        action: 'contribute',
        amount: amount,
        reasoning: agent.name + ' contributes ' + amount + ' — ' + p.archetype + ' approach.',
        agent_id: agent.id,
        agent_name: agent.name,
        personality: p.archetype
      };
    }

    // Extraction games (commons)
    if (actions.indexOf('extract') !== -1) {
      var maxE = ctx.max_extraction || 100;
      var baseE = maxE * (1 - p.cooperation_bias);
      var resLevel = ctx.resource_level != null ? ctx.resource_level : 1.0;

      if (resLevel < 0.4) {
        baseE *= 0.6 + 0.4 * p.risk_tolerance;
      }

      var noiseE = (Math.random() - 0.5) * maxE * 0.15 * p.risk_tolerance;
      var amountE = Math.round(Math.max(0, Math.min(maxE, baseE + noiseE)));

      return {
        action: 'extract',
        amount: amountE,
        reasoning: agent.name + ' extracts ' + amountE + (resLevel < 0.4 ? ' — resource is scarce.' : ' — balancing need with sustainability.'),
        agent_id: agent.id,
        agent_name: agent.name,
        personality: p.archetype
      };
    }

    // Bid games
    if (actions.indexOf('bid') !== -1) {
      var estValue = ctx.estimated_value || 100;
      var bidRatio = 0.5 + p.risk_tolerance * 0.5;
      var noiseB = (Math.random() - 0.5) * estValue * 0.2;
      var amountB = Math.round(Math.max(1, estValue * bidRatio + noiseB));

      return {
        action: 'bid',
        amount: amountB,
        reasoning: agent.name + ' bids ' + amountB + ' — ' + (p.risk_tolerance > 0.6 ? 'aggressive' : 'conservative') + ' strategy.',
        agent_id: agent.id,
        agent_name: agent.name,
        personality: p.archetype
      };
    }

    // Join/wait games (network effects)
    if (actions.indexOf('join') !== -1 && actions.indexOf('wait') !== -1) {
      var netSize = ctx.network_size != null ? ctx.network_size : 0;
      var threshold = 1 - p.risk_tolerance;
      var act = (netSize >= threshold || Math.random() < p.risk_tolerance * 0.5) ? 'join' : 'wait';

      return {
        action: act,
        amount: null,
        reasoning: agent.name + (act === 'join' ? ' joins — sees momentum.' : ' waits — needs more adoption.'),
        agent_id: agent.id,
        agent_name: agent.name,
        personality: p.archetype
      };
    }

    // Default
    return {
      action: actions[0],
      amount: null,
      reasoning: agent.name + ' chooses ' + actions[0] + '.',
      agent_id: agent.id,
      agent_name: agent.name,
      personality: p.archetype
    };
  }

  // ── API call with timeout and retry ────────────────────────────────

  function fetchWithTimeout(url, options, timeoutMs) {
    return new Promise(function (resolve, reject) {
      var timer = setTimeout(function () {
        reject(new Error('Request timed out'));
      }, timeoutMs);

      fetch(url, options)
        .then(function (resp) {
          clearTimeout(timer);
          resolve(resp);
        })
        .catch(function (err) {
          clearTimeout(timer);
          reject(err);
        });
    });
  }

  function callEdgeFunction(body, retries) {
    if (retries === undefined) retries = 0;

    return fetchWithTimeout(
      CONFIG.EDGE_FUNCTION_URL,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      },
      CONFIG.TIMEOUT
    ).then(function (resp) {
      if (!resp.ok) {
        if (resp.status === 429 && retries < CONFIG.MAX_RETRIES) {
          return new Promise(function (resolve) {
            setTimeout(resolve, CONFIG.RETRY_DELAY * (retries + 1));
          }).then(function () {
            return callEdgeFunction(body, retries + 1);
          });
        }
        throw new Error('Edge function error: ' + resp.status);
      }
      return resp.json();
    });
  }

  // ── Main class ─────────────────────────────────────────────────────

  // ── Available LLM providers (for UI display) ───────────────────────
  var LLM_PROVIDERS = [
    { id: 'auto',     name: 'Auto (cheapest available)', description: 'Automatically picks the cheapest configured provider' },
    { id: 'deepseek', name: 'DeepSeek',                  description: 'Near GPT-4 quality, very cheap (~₹0.50/1K sessions)' },
    { id: 'groq',     name: 'Groq (Llama 3.1 70B)',      description: 'Free tier, fast inference, rate-limited' },
    { id: 'gemini',   name: 'Google Gemini Flash',        description: 'Free tier available, good quality' },
    { id: 'together', name: 'Together AI',                description: 'Cheap and reliable (~₹1-3/1K sessions)' },
    { id: 'openai',   name: 'OpenAI (GPT-4o-mini)',       description: 'Premium quality' },
    { id: 'none',     name: 'No AI (personality engine)',  description: 'Free — uses personality weights only, no LLM' }
  ];

  function IMGameAgents(gameId, options) {
    this.gameId = gameId;
    this.options = options || {};
    this.useLLM = this.options.useLLM !== false;
    // Provider preference: 'auto' (default), 'deepseek', 'groq', 'gemini', 'together', 'openai', 'none'
    this.provider = this.options.provider || 'auto';
    if (this.provider === 'none') this.useLLM = false;
    this._roster = null;
  }

  /**
   * Get the roster of agents for this game (for UI display).
   * Returns a Promise resolving to an array of agent objects.
   */
  IMGameAgents.prototype.getRoster = function () {
    var self = this;

    if (self._roster) return Promise.resolve(self._roster);

    return loadAgentData().then(function (data) {
      if (!data || !data.games || !data.games[self.gameId]) {
        throw new Error('No agents found for game: ' + self.gameId);
      }

      self._roster = data.games[self.gameId].agents;
      return self._roster;
    });
  };

  /**
   * Get a single agent's decision.
   * Falls back to local engine if Edge Function is unavailable.
   */
  IMGameAgents.prototype.getDecision = function (agentId, opts) {
    var self = this;

    var body = {
      game_id: self.gameId,
      agent_id: agentId,
      round: opts.round,
      total_rounds: opts.totalRounds,
      history: opts.history || [],
      available_actions: opts.availableActions,
      context: opts.context || {},
      use_llm: self.useLLM,
      provider: self.provider !== 'auto' ? self.provider : undefined
    };

    return callEdgeFunction(body).catch(function () {
      // Fallback to local engine
      return loadAgentData().then(function (data) {
        if (!data || !data.games[self.gameId]) {
          throw new Error('Agent data unavailable');
        }

        var agents = data.games[self.gameId].agents;
        var agent = null;
        for (var i = 0; i < agents.length; i++) {
          if (agents[i].id === agentId) {
            agent = agents[i];
            break;
          }
        }

        if (!agent) throw new Error('Agent not found: ' + agentId);
        return localDecision(agent, opts);
      });
    });
  };

  /**
   * Get ALL agents' decisions for a round (parallel requests).
   * Returns a Promise resolving to { agentId: decision, ... }
   */
  IMGameAgents.prototype.getAllDecisions = function (opts) {
    var self = this;

    return self.getRoster().then(function (roster) {
      var promises = roster.map(function (agent) {
        return self.getDecision(agent.id, opts).then(function (decision) {
          return { id: agent.id, decision: decision };
        });
      });

      return Promise.all(promises).then(function (results) {
        var decisions = {};
        results.forEach(function (r) {
          decisions[r.id] = r.decision;
        });
        return decisions;
      });
    });
  };

  /**
   * Switch LLM provider at runtime.
   * @param {string} providerId - 'auto', 'deepseek', 'groq', 'gemini', 'together', 'openai', or 'none'
   */
  IMGameAgents.prototype.setProvider = function (providerId) {
    this.provider = providerId || 'auto';
    this.useLLM = providerId !== 'none';
  };

  /**
   * Get available LLM providers (for settings UI).
   * Returns array of { id, name, description }.
   */
  IMGameAgents.getProviders = function () {
    return LLM_PROVIDERS.slice(); // return a copy
  };

  /**
   * Configure the Edge Function URL (for custom deployments).
   */
  IMGameAgents.configure = function (options) {
    if (options.edgeFunctionUrl) CONFIG.EDGE_FUNCTION_URL = options.edgeFunctionUrl;
    if (options.agentDataUrl) CONFIG.AGENT_DATA_URL = options.agentDataUrl;
    if (options.timeout) CONFIG.TIMEOUT = options.timeout;
  };

  // ── Export ─────────────────────────────────────────────────────────

  window.IMGameAgents = IMGameAgents;
})();
