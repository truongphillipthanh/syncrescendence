import React, { useState } from 'react';

const ConstellationBifurcatedArchitecture = () => {
  const [highlightAccount, setHighlightAccount] = useState(null);
  const [expandedEcosystem, setExpandedEcosystem] = useState(null);
  const [expandedCLI, setExpandedCLI] = useState(null);

  const accountColors = {
    1: '#3B82F6',
    2: '#8B5CF6', 
    3: '#10B981'
  };

  const platformData = {
    'Claude': { icon: '🔶', color: '#D97706' },
    'ChatGPT': { icon: '🟢', color: '#10B981' },
    'Gemini': { icon: '🔵', color: '#3B82F6' },
    'Grok': { icon: '🔴', color: '#EF4444' },
    'Perplexity': { icon: '🟣', color: '#8B5CF6' }
  };

  const cliToolData = {
    'Claude Code': { 
      icon: '⚡', 
      color: '#D97706',
      runtime: 'Terminal-resident agent',
      models: 'Claude Opus 4.5, Sonnet 4.5'
    },
    'Codex CLI': { 
      icon: '⚙️', 
      color: '#10B981',
      runtime: 'Headless automation',
      models: 'GPT-5.2, o3/o4-mini'
    },
    'Gemini CLI': { 
      icon: '🔷', 
      color: '#3B82F6',
      runtime: 'Stateless batch processing',
      models: 'Gemini 3 Pro, Flash'
    }
  };

  const cloudEcosystemData = {
    'Claude': {
      categories: [
        {
          name: 'Browser & Desktop Agents',
          tools: ['Claude in Chrome', 'Claude in Excel', 'Cowork (file automation)']
        },
        {
          name: 'Integration',
          tools: ['MCP Protocol', 'Computer Use API', 'Extended Thinking', 'Artifacts']
        }
      ]
    },
    'ChatGPT': {
      categories: [
        {
          name: 'Creative Media',
          tools: ['Sora (video gen)', 'DALL-E 3 / GPT Image 1.5', 'Advanced Voice Mode']
        },
        {
          name: 'Research & Analysis',
          tools: ['Deep Research', 'Code Interpreter', 'Operator (browser agent)']
        },
        {
          name: 'Workspaces & Store',
          tools: ['Canvas (doc/code editor)', 'Custom GPTs', 'GPT Store']
        }
      ]
    },
    'Gemini': {
      categories: [
        {
          name: 'Google Labs',
          tools: ['NotebookLM (+ Enterprise API)', 'Illuminate (paper-to-podcast)', 'Jules (coding agent)']
        },
        {
          name: 'Creative Media',
          tools: ['ImageFX (Imagen 3)', 'VideoFX / Flow (Veo 3.1)', 'MusicFX', 'Whisk (image remix)']
        },
        {
          name: 'Google Workspace',
          tools: ['Gmail', 'Drive', 'Docs', 'Sheets', 'Slides', 'Meet', 'Calendar', 'Apps Script']
        },
        {
          name: 'Development & Research',
          tools: ['Google Colab (Pro+)', 'AI Studio', 'Vertex AI', 'Scholar PDF Reader']
        },
        {
          name: 'Browser Integration',
          tools: ['Chrome Gemini Nano', 'Chrome DevTools AI', 'YouTube integration']
        },
        {
          name: 'Enterprise',
          tools: ['Pinpoint (investigative)', 'Discovery Engine', 'BigQuery ML']
        }
      ]
    },
    'Grok': {
      categories: [
        {
          name: 'X Integration',
          tools: ['X (Twitter)', 'X Firehose (real-time)', 'X Posts context']
        },
        {
          name: 'Media',
          tools: ['Grok Image Generation', 'X Premium features']
        }
      ]
    },
    'Perplexity': {
      categories: [
        {
          name: 'Research',
          tools: ['Deep Research', 'Perplexity Pages', 'Pro Search']
        },
        {
          name: 'Integration',
          tools: ['Citation engine', 'Source verification']
        }
      ]
    }
  };

  const cliEcosystemData = {
    'Claude Code': {
      categories: [
        {
          name: 'Configuration System',
          tools: ['CLAUDE.md (hierarchical)', 'settings.json', '.claude/rules/', 'Conditional context']
        },
        {
          name: 'Execution Modes',
          tools: ['Interactive mode', 'Plan mode', 'Auto-edit mode', 'Headless execution']
        },
        {
          name: 'Integration',
          tools: ['Git worktrees', 'MCP servers', 'Skills system', 'Teleport (web↔terminal)']
        }
      ]
    },
    'Codex CLI': {
      categories: [
        {
          name: 'Execution Modes',
          tools: ['Interactive REPL', 'Suggest mode', 'Auto-edit mode', 'Full auto mode']
        },
        {
          name: 'Configuration',
          tools: ['AGENTS.md', 'Custom instructions', 'Project configs']
        },
        {
          name: 'Integration',
          tools: ['GitHub Actions', 'IDE extensions', 'Codex Cloud (web)', 'Slack bot']
        }
      ]
    },
    'Gemini CLI': {
      categories: [
        {
          name: 'API Access',
          tools: ['Gemini Pro API', 'Gemini Flash API', '1M token context', 'Multimodal inputs']
        },
        {
          name: 'Batch Processing',
          tools: ['Stateless invocation', 'Scriptable workflows', 'Corpus analysis', 'Evidence packs']
        },
        {
          name: 'Integration',
          tools: ['Apps Script connector', 'Colab integration', 'Vertex AI SDK']
        }
      ]
    }
  };

  const accounts = [
    {
      id: 1,
      email: 'truongphillipthanh@icloud.com',
      auth: 'Apple',
      platforms: ['Claude', 'ChatGPT', 'Grok', 'Perplexity'],
      cliTools: ['Claude Code', 'Codex CLI', 'Gemini CLI'],
      github: 'truongphillipthanh (primary repo)',
      color: accountColors[1]
    },
    {
      id: 2,
      email: 'icloud.truongphillipthanh@gmail.com',
      auth: 'Google',
      platforms: ['Claude', 'ChatGPT', 'Gemini', 'Grok', 'Perplexity'],
      cliTools: ['Claude Code', 'Codex CLI', 'Gemini CLI'],
      github: 'icloud-truongphillipthanh (fork)',
      color: accountColors[2]
    },
    {
      id: 3,
      email: 'truongphillipthanh@gmail.com',
      auth: 'Google',
      platforms: ['Claude', 'ChatGPT', 'Gemini', 'Grok', 'Perplexity'],
      cliTools: ['Claude Code', 'Codex CLI', 'Gemini CLI'],
      github: 'truongphillipthanh-gmail (fork)',
      color: accountColors[3]
    }
  ];

  const AccountBadge = ({ account, compact }) => (
    <div 
      className="inline-flex items-center gap-1 px-2 py-1 rounded text-xs font-mono"
      style={{ 
        backgroundColor: `${account.color}20`,
        border: `1px solid ${account.color}`,
        color: account.color
      }}
    >
      {compact ? `Acc${account.id}` : `Account ${account.id}`}
    </div>
  );

  return (
    <div className="w-full min-h-screen bg-slate-900 text-white p-8 overflow-auto font-mono">
      <div className="max-w-7xl mx-auto">
        
        {/* Title */}
        <div className="text-center mb-8">
          <h1 className="text-2xl font-bold mb-2">Syncrescendence IIC Architecture</h1>
          <p className="text-slate-400 text-sm">Cloud Ecosystem | Local CLI | Platform Services | Desktop | Repository</p>
        </div>

        {/* Legend */}
        <div className="flex justify-center gap-6 mb-8 text-xs">
          {accounts.map(acc => (
            <button
              key={acc.id}
              onClick={() => setHighlightAccount(highlightAccount === acc.id ? null : acc.id)}
              className="flex items-center gap-2 px-3 py-2 rounded bg-slate-800 hover:bg-slate-700 transition-colors"
            >
              <AccountBadge account={acc} compact />
              <span className="text-slate-400">{acc.auth} SSO</span>
            </button>
          ))}
        </div>

        <div className="relative">
          
          {/* ============ BIFURCATED ECOSYSTEM LAYER ============ */}
          <div className="mb-16">
            <div className="text-center mb-6">
              <div className="inline-block bg-gradient-to-r from-purple-900 to-blue-900 px-6 py-2 rounded-full border-2 border-purple-500">
                <span className="text-xl">🌐 PLATFORM ECOSYSTEMS</span>
              </div>
              <p className="text-xs text-slate-400 mt-2">Cloud services (left) | Local CLI tools (right)</p>
            </div>

            <div className="grid grid-cols-2 gap-8">
              
              {/* LEFT: CLOUD ECOSYSTEM */}
              <div>
                <div className="text-center mb-4">
                  <div className="inline-block bg-blue-900/50 px-4 py-2 rounded-lg border border-blue-600">
                    <span className="text-sm font-bold text-blue-300">☁️ CLOUD ECOSYSTEM</span>
                  </div>
                  <p className="text-xs text-slate-500 mt-1">Web/mobile interfaces</p>
                </div>

                <div className="grid grid-cols-1 gap-3">
                  {Object.entries(cloudEcosystemData).map(([platform, { categories }]) => (
                    <div 
                      key={platform} 
                      className="bg-slate-800 rounded-lg border-2 border-slate-700 overflow-hidden"
                      style={{ borderColor: platformData[platform].color + '40' }}
                    >
                      {/* Platform Header */}
                      <div 
                        className="p-3 cursor-pointer transition-colors"
                        style={{ backgroundColor: platformData[platform].color + '20' }}
                        onClick={() => setExpandedEcosystem(expandedEcosystem === platform ? null : platform)}
                      >
                        <div className="flex items-center justify-between">
                          <div className="flex items-center gap-2">
                            <span className="text-xl">{platformData[platform].icon}</span>
                            <span className="font-bold text-sm">{platform}</span>
                          </div>
                          <span className="text-xs text-slate-400">
                            {expandedEcosystem === platform ? '▼' : '▶'}
                          </span>
                        </div>
                        <div className="text-xs text-slate-400 mt-1">
                          {categories.reduce((sum, cat) => sum + cat.tools.length, 0)} cloud tools
                        </div>
                      </div>

                      {/* Ecosystem Tools */}
                      <div className={`transition-all duration-300 ${expandedEcosystem === platform ? 'max-h-96 overflow-auto' : 'max-h-24 overflow-hidden'}`}>
                        {categories.map((category, idx) => (
                          <div key={idx} className="p-3 border-t border-slate-700">
                            <div className="text-xs font-bold mb-2" style={{ color: platformData[platform].color }}>
                              {category.name}
                            </div>
                            <div className="space-y-1">
                              {category.tools.map((tool, toolIdx) => (
                                <div 
                                  key={toolIdx} 
                                  className="text-xs text-slate-300 pl-2 border-l-2"
                                  style={{ borderColor: platformData[platform].color + '40' }}
                                >
                                  • {tool}
                                </div>
                              ))}
                            </div>
                          </div>
                        ))}
                      </div>

                      {/* Collapse hint */}
                      {expandedEcosystem !== platform && categories.reduce((sum, cat) => sum + cat.tools.length, 0) > 3 && (
                        <div className="p-2 text-center text-xs text-slate-500 border-t border-slate-700">
                          Click to expand
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>

              {/* RIGHT: LOCAL CLI ECOSYSTEM */}
              <div>
                <div className="text-center mb-4">
                  <div className="inline-block bg-green-900/50 px-4 py-2 rounded-lg border border-green-600">
                    <span className="text-sm font-bold text-green-300">⌨️ LOCAL CLI ECOSYSTEM</span>
                  </div>
                  <p className="text-xs text-slate-500 mt-1">Terminal-based agents</p>
                </div>

                <div className="grid grid-cols-1 gap-3">
                  {Object.entries(cliEcosystemData).map(([cliTool, { categories }]) => (
                    <div 
                      key={cliTool} 
                      className="bg-slate-800 rounded-lg border-2 border-slate-700 overflow-hidden"
                      style={{ borderColor: cliToolData[cliTool].color + '40' }}
                    >
                      {/* CLI Tool Header */}
                      <div 
                        className="p-3 cursor-pointer transition-colors"
                        style={{ backgroundColor: cliToolData[cliTool].color + '20' }}
                        onClick={() => setExpandedCLI(expandedCLI === cliTool ? null : cliTool)}
                      >
                        <div className="flex items-center justify-between">
                          <div className="flex items-center gap-2">
                            <span className="text-xl">{cliToolData[cliTool].icon}</span>
                            <div>
                              <div className="font-bold text-sm">{cliTool}</div>
                              <div className="text-xs text-slate-400">{cliToolData[cliTool].runtime}</div>
                            </div>
                          </div>
                          <span className="text-xs text-slate-400">
                            {expandedCLI === cliTool ? '▼' : '▶'}
                          </span>
                        </div>
                        <div className="text-xs text-slate-400 mt-1">
                          {cliToolData[cliTool].models}
                        </div>
                      </div>

                      {/* CLI Capabilities */}
                      <div className={`transition-all duration-300 ${expandedCLI === cliTool ? 'max-h-96 overflow-auto' : 'max-h-24 overflow-hidden'}`}>
                        {categories.map((category, idx) => (
                          <div key={idx} className="p-3 border-t border-slate-700">
                            <div className="text-xs font-bold mb-2" style={{ color: cliToolData[cliTool].color }}>
                              {category.name}
                            </div>
                            <div className="space-y-1">
                              {category.tools.map((tool, toolIdx) => (
                                <div 
                                  key={toolIdx} 
                                  className="text-xs text-slate-300 pl-2 border-l-2"
                                  style={{ borderColor: cliToolData[cliTool].color + '40' }}
                                >
                                  • {tool}
                                </div>
                              ))}
                            </div>
                          </div>
                        ))}
                      </div>

                      {/* Collapse hint */}
                      {expandedCLI !== cliTool && (
                        <div className="p-2 text-center text-xs text-slate-500 border-t border-slate-700">
                          Click to expand
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>

            </div>
          </div>

          {/* Connection lines down - bifurcated */}
          <div className="flex justify-center mb-8 gap-32">
            <div className="flex flex-col items-center">
              <div className="text-xs text-blue-400 mb-2">Cloud path</div>
              <div className="w-px h-16 bg-gradient-to-b from-blue-500 to-slate-600"></div>
            </div>
            <div className="flex flex-col items-center">
              <div className="text-xs text-green-400 mb-2">Local path</div>
              <div className="w-px h-16 bg-gradient-to-b from-green-500 to-slate-600"></div>
            </div>
          </div>

          {/* ============ CLOUD PLATFORMS LAYER ============ */}
          <div className="mb-16">
            <div className="text-center mb-6">
              <div className="inline-block bg-slate-800 px-6 py-2 rounded-full">
                <span className="text-xl">☁️ CLOUD PLATFORM SERVICES</span>
              </div>
              <p className="text-xs text-slate-400 mt-1">Web/mobile chat interfaces</p>
            </div>

            <div className="grid grid-cols-5 gap-4">
              {Object.entries(platformData).map(([platform, { icon, color }]) => (
                <div key={platform} className="bg-slate-800 rounded-lg p-4">
                  <div className="text-center mb-3">
                    <div className="text-3xl mb-1">{icon}</div>
                    <div className="font-bold text-sm">{platform}</div>
                  </div>

                  {/* Show which accounts can access */}
                  <div className="space-y-2">
                    {accounts.map(acc => {
                      const canAccess = acc.platforms.includes(platform);
                      const isHighlighted = highlightAccount === acc.id;
                      const isNoGoogle = acc.id === 1 && platform === 'Gemini';
                      
                      if (!canAccess || isNoGoogle) {
                        return (
                          <div key={acc.id} className="flex items-center gap-2 opacity-30">
                            <AccountBadge account={acc} compact />
                            {isNoGoogle && <span className="text-xs text-red-400">✗ No Google</span>}
                          </div>
                        );
                      }

                      return (
                        <div 
                          key={acc.id} 
                          className={`flex items-center gap-2 transition-all ${
                            isHighlighted ? 'opacity-100 scale-105' : 
                            highlightAccount ? 'opacity-30' : 'opacity-70'
                          }`}
                        >
                          <AccountBadge account={acc} compact />
                          <div className="flex-1 h-px bg-slate-600"></div>
                          <span className="text-xs text-slate-500">{acc.auth}</span>
                        </div>
                      );
                    })}
                  </div>
                </div>
              ))}
            </div>

            {/* Auth Flow Annotations */}
            <div className="mt-4 text-center text-xs text-slate-400 space-y-1">
              <div>Account 2 & 3: <span className="text-blue-400">Sign in with Google</span> → Full cloud ecosystem (Gmail, Drive, Workspace, YouTube)</div>
              <div>Account 1: <span className="text-blue-400">Sign in with Apple</span> → Limited to non-Google platforms</div>
            </div>
          </div>

          {/* Connection lines down to hub */}
          <div className="flex justify-center mb-8">
            <div className="w-px h-16 bg-gradient-to-b from-slate-600 to-transparent"></div>
          </div>

          {/* ============ HUB LAYER ============ */}
          <div className="mb-16">
            <div className="flex justify-center mb-8">
              <div className="bg-amber-900/30 border-2 border-amber-600 rounded-2xl p-8 max-w-md">
                <div className="text-center">
                  <div className="text-5xl mb-3">🧠</div>
                  <div className="text-xl font-bold mb-2">Principal Hub</div>
                  <div className="text-sm text-slate-400 mb-4">
                    Orchestrates across:
                    <div className="mt-2">
                      <span className="text-blue-300">5 cloud platforms</span> + 
                      <span className="text-green-300"> 3 CLI tools</span>
                    </div>
                    <div className="text-xs mt-1">30+ cloud services | 3 local agents</div>
                  </div>
                  
                  <div className="grid grid-cols-3 gap-2 text-xs">
                    {accounts.map(acc => (
                      <div 
                        key={acc.id}
                        className="bg-slate-800/50 rounded p-2"
                      >
                        <AccountBadge account={acc} compact />
                        <div className="mt-1 text-slate-500">{acc.auth}</div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Connection lines down to desktop - showing CLI tools merge here */}
          <div className="flex justify-center mb-8">
            <div className="flex flex-col items-center">
              <div className="text-xs text-slate-500 mb-2">CLI tools execute here ↓</div>
              <div className="w-px h-16 bg-gradient-to-b from-amber-600/50 to-slate-600"></div>
            </div>
          </div>

          {/* ============ DESKTOP/CLI LAYER ============ */}
          <div className="mb-16">
            <div className="text-center mb-6">
              <div className="inline-block bg-slate-800 px-6 py-2 rounded-full">
                <span className="text-xl">💻 DESKTOP / CLI INTERFACE</span>
              </div>
              <div className="text-xs text-slate-400 mt-2">Physical: MacBook Air (bottom-left) ← You, Mac mini C49RG9x (top-right)</div>
              <div className="text-xs text-slate-500 mt-1">Both machines mirrored - same browsers/apps/CLI tools installed</div>
            </div>

            <div className="grid grid-cols-2 gap-6">
              {/* Mac mini */}
              <div className="bg-slate-800 rounded-lg p-4 border-2 border-blue-500">
                <div className="text-center mb-4">
                  <div className="text-3xl mb-1">🖥️</div>
                  <div className="font-bold">Mac mini (C49RG9x)</div>
                  <div className="text-xs text-slate-400">Primary: <AccountBadge account={accounts[1]} compact /></div>
                  <div className="text-xs text-blue-400 mt-1">External Monitor - Top Right</div>
                </div>
                
                <div className="space-y-3 text-sm">
                  <div className="bg-slate-900 rounded p-2">
                    <div className="text-slate-400 text-xs mb-1">Browsers (Cloud Access) - Mirrored</div>
                    <div>Orion → <AccountBadge account={accounts[1]} compact /> <span className="text-purple-400">Primary</span></div>
                    <div>Safari → <AccountBadge account={accounts[0]} compact /></div>
                    <div>Atlas+Comet → <AccountBadge account={accounts[0]} compact /></div>
                  </div>
                  
                  <div className="bg-slate-900 rounded p-2">
                    <div className="text-slate-400 text-xs mb-1">Desktop Apps (Cloud) - Mirrored</div>
                    <div>Claude Code → <AccountBadge account={accounts[1]} compact /></div>
                    <div>ChatGPT → <AccountBadge account={accounts[0]} compact /></div>
                    <div>Perplexity → <AccountBadge account={accounts[0]} compact /></div>
                  </div>

                  <div className="bg-green-900/30 rounded p-2 border border-green-600">
                    <div className="text-green-400 text-xs mb-1">⌨️ CLI (Local Agents) - Mirrored</div>
                    <div>Claude Code → <AccountBadge account={accounts[0]} compact /></div>
                    <div>Codex CLI → <AccountBadge account={accounts[0]} compact /></div>
                    <div>Gemini CLI → <AccountBadge account={accounts[2]} compact /></div>
                  </div>
                </div>
              </div>

              {/* MacBook Air */}
              <div className="bg-slate-800 rounded-lg p-4 border-2 border-green-500">
                <div className="text-center mb-4">
                  <div className="text-3xl mb-1">💻</div>
                  <div className="font-bold">MacBook Air</div>
                  <div className="text-xs text-slate-400">Primary: <AccountBadge account={accounts[2]} compact /></div>
                  <div className="text-xs text-green-400 mt-1">Built-in Display - Bottom Left</div>
                </div>
                
                <div className="space-y-3 text-sm">
                  <div className="bg-slate-900 rounded p-2">
                    <div className="text-slate-400 text-xs mb-1">Browsers (Cloud Access) - Mirrored</div>
                    <div>Chrome → <AccountBadge account={accounts[2]} compact /> <span className="text-green-400">Primary</span></div>
                    <div>Safari → <AccountBadge account={accounts[0]} compact /></div>
                    <div>Atlas+Comet → <AccountBadge account={accounts[0]} compact /></div>
                  </div>
                  
                  <div className="bg-slate-900 rounded p-2">
                    <div className="text-slate-400 text-xs mb-1">Desktop Apps (Cloud) - Mirrored</div>
                    <div>Claude Code → <AccountBadge account={accounts[2]} compact /></div>
                    <div>ChatGPT → <AccountBadge account={accounts[0]} compact /></div>
                    <div>Perplexity → <AccountBadge account={accounts[0]} compact /></div>
                  </div>

                  <div className="bg-green-900/30 rounded p-2 border border-green-600">
                    <div className="text-green-400 text-xs mb-1">⌨️ CLI (Local Agents) - Mirrored</div>
                    <div>Claude Code → <AccountBadge account={accounts[0]} compact /></div>
                    <div>Codex CLI → <AccountBadge account={accounts[0]} compact /></div>
                    <div>Gemini CLI → <AccountBadge account={accounts[2]} compact /></div>
                  </div>
                </div>
              </div>
            </div>

            <div className="mt-6 text-center">
              <div className="inline-block bg-slate-800/50 rounded px-4 py-2 text-sm">
                <div className="text-slate-400 mb-1">Repository Location</div>
                <div className="font-mono text-green-400">~/Desktop/syncrescendence/</div>
                <div className="text-xs text-slate-500 mt-1">Unified across both devices, <AccountBadge account={accounts[0]} compact /> owns primary</div>
              </div>
            </div>
          </div>

          {/* Connection lines down to repo */}
          <div className="flex justify-center mb-8">
            <div className="relative w-64 h-24">
              <svg className="absolute inset-0 w-full h-full">
                <line x1="50%" y1="0" x2="50%" y2="100%" stroke="#475569" strokeWidth="2" strokeDasharray="4 4" />
                <text x="50%" y="50%" fill="#94a3b8" fontSize="12" textAnchor="middle">git push/pull</text>
              </svg>
            </div>
          </div>

          {/* ============ REPOSITORY LAYER ============ */}
          <div className="mb-8">
            <div className="text-center mb-6">
              <div className="inline-block bg-slate-800 px-6 py-2 rounded-full">
                <span className="text-xl">📦 REPOSITORY (Below the Iceberg)</span>
              </div>
            </div>

            <div className="bg-gradient-to-b from-slate-800 to-slate-900 rounded-lg p-6 border-2 border-slate-700">
              
              {/* GitHub remotes */}
              <div className="grid grid-cols-3 gap-4 mb-6">
                <div className="bg-slate-950 rounded p-4 border-2 border-blue-600">
                  <div className="text-center mb-2">
                    <div className="text-2xl mb-1">📍</div>
                    <div className="font-bold text-sm text-blue-400">Primary Remote</div>
                  </div>
                  <div className="space-y-2 text-xs">
                    <AccountBadge account={accounts[0]} />
                    <div className="text-slate-400 font-mono">github.com/truongphillipthanh/syncrescendence</div>
                    <div className="text-green-400">← Desktop pushes here</div>
                  </div>
                </div>

                <div className="bg-slate-950 rounded p-4 border border-purple-600">
                  <div className="text-center mb-2">
                    <div className="text-2xl mb-1">🔄</div>
                    <div className="font-bold text-sm text-purple-400">Fork</div>
                  </div>
                  <div className="space-y-2 text-xs">
                    <AccountBadge account={accounts[1]} />
                    <div className="text-slate-400 font-mono">github.com/icloud-truong../syncrescendence</div>
                    <div className="text-purple-400">← Cloned from Acc1</div>
                  </div>
                </div>

                <div className="bg-slate-950 rounded p-4 border border-green-600">
                  <div className="text-center mb-2">
                    <div className="text-2xl mb-1">🔄</div>
                    <div className="font-bold text-sm text-green-400">Fork</div>
                  </div>
                  <div className="space-y-2 text-xs">
                    <AccountBadge account={accounts[2]} />
                    <div className="text-slate-400 font-mono">github.com/truongphillip../syncrescendence</div>
                    <div className="text-green-400">← Cloned from Acc1</div>
                  </div>
                </div>
              </div>

              {/* Repo contents */}
              <div className="bg-slate-950 rounded-lg p-4 font-mono text-sm">
                <div className="text-slate-400 mb-3 text-xs">Repository Structure (local ~/Desktop/syncrescendence/)</div>
                <div className="space-y-1 text-slate-300">
                  <div>├── <span className="text-amber-400">00-ORCHESTRATION/</span> <span className="text-slate-500">← System state, active configs</span></div>
                  <div>├── <span className="text-blue-400">01-CANON/</span> <span className="text-slate-500">← Protected scripture (148k words)</span></div>
                  <div>├── <span className="text-green-400">02-OPERATIONAL/</span> <span className="text-slate-500">← Prompts, constellation configs</span></div>
                  <div>├── <span className="text-purple-400">03-PROJECTS/</span> <span className="text-slate-500">← Active development</span></div>
                  <div>├── <span className="text-slate-400">04-SOURCES/</span> <span className="text-slate-500">← Research, working material</span></div>
                  <div>├── <span className="text-slate-600">05-ARCHIVE/</span> <span className="text-slate-500">← Historical artifacts</span></div>
                  <div>├── <span className="text-yellow-400">-INBOX/</span> <span className="text-slate-500">← Handoffs from web apps</span></div>
                  <div>├── <span className="text-yellow-400">-OUTGOING/</span> <span className="text-slate-500">← Evidence packs for distribution</span></div>
                  <div>├── <span className="text-slate-300">CLAUDE.md</span> <span className="text-slate-500">← Claude Code directives</span></div>
                  <div>├── <span className="text-slate-300">GEMINI.md</span> <span className="text-slate-500">← Gemini CLI context</span></div>
                  <div>├── <span className="text-slate-300">COCKPIT.md</span> <span className="text-slate-500">← System overview</span></div>
                  <div>└── <span className="text-slate-300">Makefile</span> <span className="text-slate-500">← Operational automation</span></div>
                </div>
              </div>

              <div className="mt-4 text-center text-xs text-slate-400">
                <div>Repository contains 28 canonical artifacts (98% complete)</div>
                <div className="mt-1">
                  <span className="text-blue-300">Cloud platforms</span> → <span className="text-yellow-400">-INBOX/</span> → Review → Git commit
                </div>
                <div>
                  <span className="text-green-300">CLI tools</span> → Direct file edits → Git commit
                </div>
                <div className="text-xs text-slate-500 mt-1">
                  Note: Gemini CLI uses Account 3 API key (Google AI Pro subscription)
                </div>
                <div className="mt-1">
                  All paths → Push to Account 1 GitHub → Forks sync
                </div>
              </div>
            </div>
          </div>

          {/* Info panel */}
          <div className="mt-8 bg-slate-800/50 rounded-lg p-6 text-sm">
            <div className="font-bold mb-3">Architecture Notes: Cloud vs Local Bifurcation</div>
            <div className="space-y-2 text-slate-400">
              <div>• <span className="text-blue-400">Cloud Ecosystem (Left)</span>: 30+ web/mobile services requiring network calls and cloud authentication</div>
              <div>• <span className="text-green-400">Local CLI Ecosystem (Right)</span>: 3 terminal-resident agents executing on Desktop/CLI layer with local file access</div>
              <div>• <span className="text-purple-400">Cloud Platforms</span>: Chat interfaces accessible via browsers/mobile apps (5 platforms, all accounts)</div>
              <div>• <span className="text-amber-400">Hub Orchestration</span>: Principal routes work to cloud services OR local CLI based on task requirements</div>
              <div>• <span className="text-cyan-400">Mirrored Desktops</span>: Both Mac mini and MacBook Air have identical browser/app/CLI installations—only difference is Claude Code account bindings</div>
              <div>• <span className="text-green-300">CLI Authentication</span>: Claude Code → Acc1 | Codex CLI → Acc1 | Gemini CLI → Acc3 (Google AI Pro)</div>
              <div>• <span className="text-yellow-400">Data Flow</span>: Cloud → -INBOX/ → Git | CLI → Direct edits → Git | Both → GitHub primary → Forks</div>
            </div>
          </div>

        </div>
      </div>
    </div>
  );
};

export default ConstellationBifurcatedArchitecture;
