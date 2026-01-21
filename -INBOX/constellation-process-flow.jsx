import React, { useState } from 'react';

const ConstellationProcessFlow = () => {
  const [highlightedPhase, setHighlightedPhase] = useState(null);

  const accountColors = {
    1: '#3B82F6',
    2: '#8B5CF6', 
    3: '#10B981'
  };

  const accounts = [
    { id: 1, color: accountColors[1], label: 'Acc1' },
    { id: 2, color: accountColors[2], label: 'Acc2' },
    { id: 3, color: accountColors[3], label: 'Acc3' }
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

  const PhaseCard = ({ phase, title, description, color, children, position }) => {
    const isHighlighted = highlightedPhase === phase;
    return (
      <div 
        className={`relative transition-all duration-300 ${isHighlighted ? 'scale-105 z-10' : 'scale-100'}`}
        onMouseEnter={() => setHighlightedPhase(phase)}
        onMouseLeave={() => setHighlightedPhase(null)}
        style={{ gridArea: position }}
      >
        <div 
          className="rounded-lg p-4 border-2"
          style={{ 
            backgroundColor: `${color}10`,
            borderColor: isHighlighted ? color : `${color}60`
          }}
        >
          <div className="flex items-center gap-2 mb-2">
            <div 
              className="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold"
              style={{ backgroundColor: `${color}30`, color: color }}
            >
              {phase}
            </div>
            <div>
              <div className="font-bold text-sm">{title}</div>
              <div className="text-xs text-slate-400">{description}</div>
            </div>
          </div>
          {children}
        </div>
      </div>
    );
  };

  const Arrow = ({ direction = 'down', label, color = '#94a3b8' }) => (
    <div className="flex flex-col items-center justify-center py-2">
      {direction === 'down' && (
        <>
          <div className="text-xs text-slate-400 mb-1">{label}</div>
          <div className="text-2xl" style={{ color }}>↓</div>
        </>
      )}
      {direction === 'up' && (
        <>
          <div className="text-2xl" style={{ color }}>↑</div>
          <div className="text-xs text-slate-400 mt-1">{label}</div>
        </>
      )}
      {direction === 'right' && (
        <>
          <div className="text-2xl" style={{ color }}>→</div>
          <div className="text-xs text-slate-400">{label}</div>
        </>
      )}
      {direction === 'cycle' && (
        <>
          <div className="text-2xl" style={{ color }}>🔄</div>
          <div className="text-xs text-slate-400 mt-1">{label}</div>
        </>
      )}
    </div>
  );

  return (
    <div className="w-full min-h-screen bg-slate-900 text-white p-8 overflow-auto font-mono">
      <div className="max-w-6xl mx-auto">
        
        {/* Title */}
        <div className="text-center mb-8">
          <h1 className="text-2xl font-bold mb-2">IIC Constellation: Process Flow</h1>
          <p className="text-slate-400 text-sm">Cloud Loop → CLI Execution → Repository Sync</p>
        </div>

        {/* Legend */}
        <div className="flex justify-center gap-6 mb-8 text-xs">
          <div className="flex items-center gap-2 bg-slate-800 px-3 py-2 rounded">
            <div className="w-3 h-3 rounded-full bg-blue-500"></div>
            <span>Interpretation</span>
          </div>
          <div className="flex items-center gap-2 bg-slate-800 px-3 py-2 rounded">
            <div className="w-3 h-3 rounded-full bg-green-500"></div>
            <span>Design/Structure</span>
          </div>
          <div className="flex items-center gap-2 bg-slate-800 px-3 py-2 rounded">
            <div className="w-3 h-3 rounded-full bg-purple-500"></div>
            <span>Decode/Audize</span>
          </div>
          <div className="flex items-center gap-2 bg-slate-800 px-3 py-2 rounded">
            <div className="w-3 h-3 rounded-full bg-amber-500"></div>
            <span>CLI Execution</span>
          </div>
        </div>

        <div className="space-y-6">

          {/* ========== PHASE 0: INITIATION ========== */}
          <PhaseCard phase="0" title="Initiation" description="Principal launches ideation" color="#64748b">
            <div className="mt-3 space-y-2 text-sm">
              <div className="bg-slate-800/50 rounded p-2">
                <div className="text-slate-300">🧠 <strong>Principal</strong></div>
                <div className="text-xs text-slate-400 mt-1">Identifies work requiring constellation orchestration</div>
              </div>
              <div className="text-xs text-slate-500 mt-2">
                <strong>Triggers:</strong> Complex synthesis, multi-format output, large-scale research, systematic documentation
              </div>
            </div>
          </PhaseCard>

          <Arrow direction="down" label="Initial query" color="#64748b" />

          {/* ========== CLOUD WEB APP LOOP ========== */}
          <div className="bg-slate-800/30 rounded-xl p-6 border-2 border-blue-500">
            <div className="text-center mb-4">
              <div className="inline-block bg-blue-900/50 px-4 py-2 rounded-lg border border-blue-500">
                <span className="text-lg font-bold text-blue-300">☁️ CLOUD WEB APP LOOP</span>
              </div>
              <p className="text-xs text-slate-400 mt-2">Iterative interpretation, design, and decoding cycle</p>
            </div>

            <div className="grid grid-cols-1 gap-4">

              {/* PHASE 1: CLAUDE WEB - INTERPRETATION */}
              <PhaseCard phase="1" title="Claude Web (Interpret)" description="Primary ideation interface" color="#3B82F6">
                <div className="mt-3 space-y-2 text-sm">
                  <div className="bg-slate-800/50 rounded p-2">
                    <div className="flex items-center gap-2">
                      <span className="text-xl">🔶</span>
                      <div>
                        <div className="font-bold">Claude Web</div>
                        <AccountBadge account={accounts[2]} compact />
                      </div>
                    </div>
                  </div>
                  <div className="space-y-1 text-xs">
                    <div><strong>Role:</strong> INTERPRETER - Messy ideation → structured understanding</div>
                    <div><strong>Strengths:</strong> Project memory, past chat search, synthesis, rapport-driven work</div>
                    <div><strong>Output:</strong> Conceptual framework, architectural decisions, specifications</div>
                  </div>
                  <div className="mt-2 p-2 bg-blue-900/30 rounded border border-blue-700 text-xs">
                    <strong>Decision Point:</strong>
                    <div className="mt-1 space-y-1 text-slate-300">
                      • Need external verification? → <span className="text-amber-400">Perplexity for fact-checking</span>
                      <div>• Need real-time context? → <span className="text-red-400">Grok for X firehose data</span></div>
                      <div>• Ready for structure? → <span className="text-green-400">Continue to Phase 2</span></div>
                    </div>
                  </div>
                </div>
              </PhaseCard>

              <Arrow direction="down" label="Specifications ready" color="#3B82F6" />

              {/* PHASE 2: CHATGPT WEB - DESIGN */}
              <PhaseCard phase="2" title="ChatGPT Web (Design)" description="Mechanical transformation" color="#10B981">
                <div className="mt-3 space-y-2 text-sm">
                  <div className="bg-slate-800/50 rounded p-2">
                    <div className="flex items-center gap-2">
                      <span className="text-xl">🟢</span>
                      <div>
                        <div className="font-bold">ChatGPT Web</div>
                        <AccountBadge account={accounts[0]} compact />
                      </div>
                    </div>
                  </div>
                  <div className="space-y-1 text-xs">
                    <div><strong>Role:</strong> COMPILER - Complete specs → formatted artifacts</div>
                    <div><strong>Strengths:</strong> Template execution, formatting, deterministic output</div>
                    <div><strong>Output:</strong> Structured documents, formatted artifacts, Canvas outputs</div>
                  </div>
                  <div className="mt-2 p-2 bg-green-900/30 rounded border border-green-700 text-xs">
                    <strong>Decision Point:</strong>
                    <div className="mt-1 space-y-1 text-slate-300">
                      • Need visual/video content? → <span className="text-green-400">Use Sora/DALL-E in ChatGPT</span>
                      <div>• Structure complete? → <span className="text-purple-400">Continue to Phase 3</span></div>
                      <div>• Need iteration? → <span className="text-blue-400">Loop back to Claude (Phase 1)</span></div>
                    </div>
                  </div>
                </div>
              </PhaseCard>

              <Arrow direction="down" label="Artifact created" color="#10B981" />

              {/* PHASE 3: GEMINI WEB - DECODE + AUDIZE */}
              <PhaseCard phase="3" title="Gemini Web (Decode + Audize)" description="Clarity + digestibility" color="#8B5CF6">
                <div className="mt-3 space-y-2 text-sm">
                  <div className="bg-slate-800/50 rounded p-2">
                    <div className="flex items-center gap-2">
                      <span className="text-xl">🔵</span>
                      <div>
                        <div className="font-bold">Gemini Web</div>
                        <AccountBadge account={accounts[2]} compact />
                      </div>
                    </div>
                  </div>
                  <div className="space-y-1 text-xs">
                    <div><strong>Role:</strong> DIGESTOR - Complex → digestible, text → audio</div>
                    <div><strong>Strengths:</strong> 1M token context, infinite threads, TTS optimization, NotebookLM integration</div>
                    <div><strong>Output:</strong> Simplified summaries, audio overviews, digestible formats</div>
                  </div>
                  <div className="mt-2 p-2 bg-purple-900/30 rounded border border-purple-700 text-xs">
                    <strong>Decision Point:</strong>
                    <div className="mt-1 space-y-1 text-slate-300">
                      • Need podcast/audio? → <span className="text-purple-400">NotebookLM Audio Overview</span>
                      <div>• Need corpus analysis? → <span className="text-amber-400">Prepare for Gemini CLI (Phase 5)</span></div>
                      <div>• Ready to implement? → <span className="text-cyan-400">Download & handoff to CLI (Phase 4)</span></div>
                      <div>• Need more refinement? → <span className="text-blue-400">Loop back to Claude (Phase 1)</span></div>
                    </div>
                  </div>
                </div>
              </PhaseCard>

              <div className="mt-4 text-center">
                <Arrow direction="cycle" label="Loop until satisfied" color="#8B5CF6" />
                <div className="text-xs text-slate-400 mt-2">
                  Phases 1-3 repeat iteratively until output meets requirements
                </div>
              </div>

            </div>
          </div>

          <Arrow direction="down" label="Cloud work complete - download artifacts" color="#06b6d4" />

          {/* ========== CLI EXECUTION PHASE ========== */}
          <div className="bg-slate-800/30 rounded-xl p-6 border-2 border-amber-500">
            <div className="text-center mb-4">
              <div className="inline-block bg-amber-900/50 px-4 py-2 rounded-lg border border-amber-500">
                <span className="text-lg font-bold text-amber-300">⌨️ LOCAL CLI EXECUTION</span>
              </div>
              <p className="text-xs text-slate-400 mt-2">High-volume implementation, batch processing, repository operations</p>
            </div>

            <div className="grid grid-cols-1 gap-4">

              {/* PHASE 4: CODEX CLI - RAPID IMPLEMENTATION */}
              <PhaseCard phase="4" title="Codex CLI (Rapid Implementation)" description="Parallel execution for scale" color="#10B981">
                <div className="mt-3 space-y-2 text-sm">
                  <div className="bg-slate-800/50 rounded p-2">
                    <div className="flex items-center gap-2">
                      <span className="text-xl">⚙️</span>
                      <div>
                        <div className="font-bold">Codex CLI</div>
                        <AccountBadge account={accounts[0]} compact />
                      </div>
                    </div>
                  </div>
                  <div className="space-y-1 text-xs">
                    <div><strong>Role:</strong> Headless parallel execution for high-volume implementation</div>
                    <div><strong>Strengths:</strong> Fast iteration, parallel operations, GitHub integration, 1M token context</div>
                    <div><strong>Use Cases:</strong> Bulk file creation, batch refactoring, automated testing, rapid prototyping</div>
                  </div>
                  <div className="mt-2 p-2 bg-green-900/30 rounded border border-green-700 text-xs">
                    <strong>Workflow:</strong>
                    <div className="mt-1 space-y-1 text-slate-300">
                      1. Download specifications from ChatGPT Canvas / Gemini Web
                      <div>2. Execute headless batch operations via AGENTS.md config</div>
                      <div>3. Output artifacts to repository -OUTGOING/</div>
                    </div>
                  </div>
                </div>
              </PhaseCard>

              <div className="flex items-center justify-center">
                <div className="text-slate-500 text-xs">Parallel execution ⇄</div>
              </div>

              {/* PHASE 5: CLAUDE CODE + GEMINI CLI - REFINEMENT */}
              <PhaseCard phase="5" title="Claude Code + Gemini CLI (Refinement)" description="Quality assurance & corpus work" color="#D97706">
                <div className="mt-3 space-y-2 text-sm">
                  <div className="grid grid-cols-2 gap-2">
                    <div className="bg-slate-800/50 rounded p-2">
                      <div className="flex items-center gap-2">
                        <span className="text-lg">⚡</span>
                        <div>
                          <div className="font-bold text-xs">Claude Code</div>
                          <AccountBadge account={accounts[0]} compact />
                        </div>
                      </div>
                      <div className="text-xs text-slate-400 mt-1">Mesoscopic implementation</div>
                    </div>
                    <div className="bg-slate-800/50 rounded p-2">
                      <div className="flex items-center gap-2">
                        <span className="text-lg">🔷</span>
                        <div>
                          <div className="font-bold text-xs">Gemini CLI</div>
                          <AccountBadge account={accounts[2]} compact />
                        </div>
                      </div>
                      <div className="text-xs text-slate-400 mt-1">Corpus surveys (ORACLE)</div>
                    </div>
                  </div>
                  <div className="space-y-1 text-xs">
                    <div><strong>Claude Code Role:</strong> Repository-aware editing, context preservation, quality refinement</div>
                    <div><strong>Gemini CLI Role:</strong> Stateless 1M token corpus analysis, evidence pack generation</div>
                    <div><strong>Use Cases:</strong> Debugging Codex output, architectural verification, corpus-wide queries</div>
                  </div>
                  <div className="mt-2 p-2 bg-amber-900/30 rounded border border-amber-700 text-xs">
                    <strong>Workflow:</strong>
                    <div className="mt-1 space-y-1 text-slate-300">
                      1. Claude Code reviews Codex output in CLAUDE.md context
                      <div>2. Gemini CLI runs corpus-wide analysis (e.g., "find all references to X")</div>
                      <div>3. Iterate until quality standards met</div>
                    </div>
                  </div>
                </div>
              </PhaseCard>

            </div>
          </div>

          <Arrow direction="down" label="git commit → push to GitHub" color="#06b6d4" />

          {/* ========== PHASE 6: REPOSITORY SYNC ========== */}
          <PhaseCard phase="6" title="Repository Sync" description="Consolidate & distribute" color="#06b6d4">
            <div className="mt-3 space-y-2 text-sm">
              <div className="bg-slate-800/50 rounded p-2">
                <div className="text-center">
                  <div className="text-2xl mb-1">📦</div>
                  <div className="font-bold">~/Desktop/syncrescendence/</div>
                  <div className="text-xs text-slate-400">Unified local repository → Account 1 GitHub primary</div>
                </div>
              </div>
              <div className="space-y-1 text-xs">
                <div><strong>Actions:</strong></div>
                <div className="pl-3 space-y-1 text-slate-300">
                  • CLI tools commit directly to repository
                  <div>• Cloud artifacts saved to -INBOX/, manually reviewed, then committed</div>
                  <div>• All changes pushed to Account 1 GitHub (primary remote)</div>
                  <div>• Account 2 & 3 forks automatically sync</div>
                </div>
              </div>
            </div>
          </PhaseCard>

          <Arrow direction="down" label="Work product complete" color="#22c55e" />

          {/* ========== PHASE 7: COMPLETION ========== */}
          <PhaseCard phase="7" title="Completion & Loop" description="Deliver or iterate" color="#22c55e">
            <div className="mt-3 space-y-2 text-sm">
              <div className="bg-slate-800/50 rounded p-2">
                <div className="text-slate-300">✅ <strong>Deliverable Ready</strong></div>
                <div className="text-xs text-slate-400 mt-1">Final artifacts in repository, accessible across all accounts & devices</div>
              </div>
              <div className="mt-2 p-2 bg-green-900/30 rounded border border-green-700 text-xs">
                <strong>Next Steps:</strong>
                <div className="mt-1 space-y-1 text-slate-300">
                  • Work product complete? → <span className="text-green-400">Done</span>
                  <div>• Need iteration? → <span className="text-blue-400">Return to Phase 1 (Claude Web)</span></div>
                  <div>• New related work? → <span className="text-cyan-400">Start fresh loop with updated context</span></div>
                </div>
              </div>
            </div>
          </PhaseCard>

        </div>

        {/* ========== AUXILIARY PLATFORMS (GROK / PERPLEXITY) ========== */}
        <div className="mt-12 bg-slate-800/30 rounded-xl p-6 border-2 border-slate-600">
          <div className="text-center mb-4">
            <div className="inline-block bg-slate-700/50 px-4 py-2 rounded-lg border border-slate-500">
              <span className="text-lg font-bold text-slate-300">🔀 AUXILIARY PLATFORMS</span>
            </div>
            <p className="text-xs text-slate-400 mt-2">Invoked on-demand within cloud loop</p>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div className="bg-slate-800/50 rounded p-4">
              <div className="flex items-center gap-2 mb-2">
                <span className="text-2xl">🔴</span>
                <div>
                  <div className="font-bold">Grok</div>
                  <AccountBadge account={accounts[2]} compact />
                </div>
              </div>
              <div className="text-xs space-y-1 text-slate-300">
                <div><strong>Role:</strong> Real-time X context, trend analysis, sentiment detection</div>
                <div><strong>When:</strong> Phase 1 (Claude interprets) needs current social context</div>
                <div><strong>Unique Strength:</strong> X Firehose access, 2M token context, creative ideation</div>
              </div>
            </div>

            <div className="bg-slate-800/50 rounded p-4">
              <div className="flex items-center gap-2 mb-2">
                <span className="text-2xl">🟣</span>
                <div>
                  <div className="font-bold">Perplexity</div>
                  <AccountBadge account={accounts[0]} compact />
                </div>
              </div>
              <div className="text-xs space-y-1 text-slate-300">
                <div><strong>Role:</strong> Fast fact-checking, citation-backed research, external verification</div>
                <div><strong>When:</strong> Any phase needs quick authoritative sources</div>
                <div><strong>Unique Strength:</strong> Pro Search (5-20 min deep research), citation engine</div>
              </div>
            </div>
          </div>
        </div>

        {/* ========== PROCESS SUMMARY ========== */}
        <div className="mt-8 bg-slate-800/50 rounded-lg p-6 text-sm">
          <div className="font-bold mb-3">Process Flow Summary</div>
          <div className="space-y-2 text-slate-400">
            <div>
              <span className="text-blue-400">Phases 1-3 (Cloud Loop):</span> Iterative interpretation, design, and decoding. 
              Loop continues until specifications are complete and output is digestible.
            </div>
            <div>
              <span className="text-amber-400">Phases 4-5 (CLI Execution):</span> Download artifacts from cloud. 
              Codex CLI handles bulk implementation in parallel. Claude Code + Gemini CLI refine and verify quality.
            </div>
            <div>
              <span className="text-cyan-400">Phase 6 (Repository Sync):</span> All work committed to Git, 
              pushed to Account 1 GitHub, distributed to forked repos.
            </div>
            <div>
              <span className="text-green-400">Phase 7 (Completion):</span> Deliverable ready or return to Phase 1 for iteration.
            </div>
            <div className="mt-4 pt-4 border-t border-slate-700">
              <span className="text-purple-400">Auxiliary Platforms (Grok/Perplexity):</span> Invoked on-demand within 
              Phases 1-3 for real-time context, fact-checking, or external verification. Not part of sequential flow.
            </div>
          </div>
        </div>

      </div>
    </div>
  );
};

export default ConstellationProcessFlow;
