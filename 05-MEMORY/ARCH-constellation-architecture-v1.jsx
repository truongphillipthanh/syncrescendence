import React, { useState } from 'react';

const ConstellationArchitecture = () => {
  const [activeLayer, setActiveLayer] = useState(null);
  
  const layers = {
    memory: {
      name: 'Memory Architecture',
      color: '#3b82f6',
      items: [
        { platform: 'Claude', layers: ['Project Knowledge', 'Past Chat Search', 'Thread ~200K'] },
        { platform: 'ChatGPT', layers: ['Project Files', 'PROJECT-ONLY Mode', 'Canvas'] },
        { platform: 'Gemini', layers: ['Gem Instructions', 'Drive Links (LIVE)', '1M Context'] },
        { platform: 'CLI', layers: ['CLAUDE.md', 'AGENTS.md', 'Stateless'] }
      ]
    },
    roles: {
      name: 'Constellation Roles',
      color: '#10b981',
      items: [
        { role: 'INTERPRETER', platform: 'Claude Web', account: '3', icon: '🔮' },
        { role: 'COMPILER', platform: 'ChatGPT Web', account: '1', icon: '⚙️' },
        { role: 'DIGESTOR', platform: 'Gemini Web', account: '3', icon: '📖' },
        { role: 'ORACLE', platform: 'Gemini CLI', account: '3', icon: '👁️' },
        { role: 'EXECUTOR-LEAD', platform: 'Claude Code', account: '3', icon: '⚡' },
        { role: 'PARALLEL-EXEC', platform: 'Claude Code ×2', account: '2', icon: '⚡⚡' },
        { role: 'RED TEAM', platform: 'Grok', account: '1', icon: '🎯' },
        { role: 'VERIFIER', platform: 'Perplexity', account: '-', icon: '✓' }
      ]
    },
    automation: {
      name: 'Automation Layer',
      color: '#f59e0b',
      items: [
        { tool: 'rclone', purpose: 'Drive Sync', status: 'TO_CONFIG' },
        { tool: 'Make', purpose: 'Task Orchestration', status: 'TO_CREATE' },
        { tool: 'Git Hooks', purpose: 'State Capture', status: 'TO_CREATE' },
        { tool: 'Keyboard Maestro', purpose: 'Macro Automation', status: 'AVAILABLE' },
        { tool: 'Hazel', purpose: 'Watch Folders', status: 'AVAILABLE' },
        { tool: 'Stream Deck', purpose: 'Physical Triggers', status: 'AVAILABLE' },
        { tool: 'n8n', purpose: 'Workflow Automation', status: 'AVAILABLE' },
        { tool: 'TextExpander', purpose: 'Snippet Insertion', status: 'AVAILABLE' }
      ]
    },
    states: {
      name: 'State Machine',
      color: '#8b5cf6',
      items: [
        { state: 'CAPTURED', next: 'INTERPRETED', via: 'Claude Web' },
        { state: 'INTERPRETED', next: 'COMPILED', via: 'ChatGPT Web' },
        { state: 'INTERPRETED', next: 'DIGESTED', via: 'Gemini Web' },
        { state: 'INTERPRETED', next: 'SENSED', via: 'Gemini CLI' },
        { state: 'COMPILED', next: 'STAGED', via: 'Download' },
        { state: 'STAGED', next: 'COMMITTED', via: 'Claude Code' }
      ]
    }
  };

  const accounts = [
    { id: 1, email: 'truongphillipthanh@icloud.com', auth: 'Apple', color: '#64748b' },
    { id: 2, email: 'icloud.truongphillipthanh@gmail.com', auth: 'Google', color: '#ea4335' },
    { id: 3, email: 'truongphillipthanh@gmail.com', auth: 'Google', color: '#34a853' }
  ];

  return (
    <div className="min-h-screen bg-gray-950 text-white p-6">
      <h1 className="text-2xl font-bold mb-6 text-center">Syncrescendence Constellation Architecture</h1>
      
      {/* Account Legend */}
      <div className="flex justify-center gap-4 mb-8">
        {accounts.map(acc => (
          <div key={acc.id} className="flex items-center gap-2 px-3 py-1 rounded-full" 
               style={{ backgroundColor: acc.color + '30', border: `1px solid ${acc.color}` }}>
            <span className="font-mono text-sm">Acc{acc.id}</span>
            <span className="text-xs opacity-70">{acc.auth}</span>
          </div>
        ))}
      </div>

      {/* Layer Tabs */}
      <div className="flex justify-center gap-2 mb-6">
        {Object.entries(layers).map(([key, layer]) => (
          <button
            key={key}
            onClick={() => setActiveLayer(activeLayer === key ? null : key)}
            className="px-4 py-2 rounded-lg transition-all"
            style={{
              backgroundColor: activeLayer === key ? layer.color : 'transparent',
              border: `2px solid ${layer.color}`,
              opacity: activeLayer && activeLayer !== key ? 0.5 : 1
            }}
          >
            {layer.name}
          </button>
        ))}
      </div>

      {/* Main Visualization */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        
        {/* Roles Panel */}
        <div className="bg-gray-900 rounded-xl p-4 border border-gray-800">
          <h2 className="text-lg font-semibold mb-4 text-emerald-400">🌐 Constellation Roles</h2>
          <div className="grid grid-cols-2 gap-3">
            {layers.roles.items.map((item, i) => (
              <div key={i} className="bg-gray-800 rounded-lg p-3 border border-gray-700 hover:border-emerald-500 transition-all">
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-xl">{item.icon}</span>
                  <span className="font-semibold text-sm">{item.role}</span>
                </div>
                <div className="text-xs text-gray-400">{item.platform}</div>
                <div className="text-xs mt-1">
                  <span className="px-2 py-0.5 rounded" 
                        style={{ 
                          backgroundColor: item.account === '1' ? '#64748b30' : 
                                          item.account === '2' ? '#ea433530' : 
                                          item.account === '3' ? '#34a85330' : '#52525b30'
                        }}>
                    {item.account === '-' ? 'Any' : `Acc${item.account}`}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Memory Panel */}
        <div className="bg-gray-900 rounded-xl p-4 border border-gray-800">
          <h2 className="text-lg font-semibold mb-4 text-blue-400">🧠 Memory Architecture</h2>
          <div className="space-y-3">
            {layers.memory.items.map((item, i) => (
              <div key={i} className="bg-gray-800 rounded-lg p-3 border border-gray-700">
                <div className="font-semibold text-sm mb-2">{item.platform}</div>
                <div className="flex flex-wrap gap-2">
                  {item.layers.map((layer, j) => (
                    <span key={j} className="text-xs px-2 py-1 bg-blue-900/50 rounded border border-blue-700">
                      {layer}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* State Flow Panel */}
        <div className="bg-gray-900 rounded-xl p-4 border border-gray-800">
          <h2 className="text-lg font-semibold mb-4 text-purple-400">🔄 State Machine</h2>
          <div className="space-y-2">
            {layers.states.items.map((item, i) => (
              <div key={i} className="flex items-center gap-2 text-sm">
                <span className="px-2 py-1 bg-purple-900/50 rounded border border-purple-700 font-mono">
                  {item.state}
                </span>
                <span className="text-gray-500">→</span>
                <span className="text-xs text-gray-400">({item.via})</span>
                <span className="text-gray-500">→</span>
                <span className="px-2 py-1 bg-purple-900/50 rounded border border-purple-700 font-mono">
                  {item.next}
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* Automation Panel */}
        <div className="bg-gray-900 rounded-xl p-4 border border-gray-800">
          <h2 className="text-lg font-semibold mb-4 text-amber-400">🤖 Automation Tools</h2>
          <div className="grid grid-cols-2 gap-2">
            {layers.automation.items.map((item, i) => (
              <div key={i} className="bg-gray-800 rounded-lg p-2 border border-gray-700 flex items-center justify-between">
                <div>
                  <div className="font-semibold text-xs">{item.tool}</div>
                  <div className="text-xs text-gray-500">{item.purpose}</div>
                </div>
                <span className={`text-xs px-2 py-0.5 rounded ${
                  item.status === 'AVAILABLE' ? 'bg-green-900/50 text-green-400' : 'bg-yellow-900/50 text-yellow-400'
                }`}>
                  {item.status === 'AVAILABLE' ? '✓' : '○'}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Handoff Flow */}
      <div className="mt-6 bg-gray-900 rounded-xl p-4 border border-gray-800">
        <h2 className="text-lg font-semibold mb-4 text-center">📡 Handoff Protocol</h2>
        <div className="flex items-center justify-center gap-2 flex-wrap">
          <div className="px-4 py-2 bg-blue-900/50 rounded-lg border border-blue-600">
            <div className="text-xs text-gray-400">INTERPRETER</div>
            <div className="font-semibold">Claude Web</div>
          </div>
          <div className="text-2xl">→</div>
          <div className="px-3 py-1 bg-gray-800 rounded text-xs">Token + Full Spec</div>
          <div className="text-2xl">→</div>
          <div className="px-4 py-2 bg-orange-900/50 rounded-lg border border-orange-600">
            <div className="text-xs text-gray-400">COMPILER</div>
            <div className="font-semibold">ChatGPT Web</div>
          </div>
          <div className="text-2xl">→</div>
          <div className="px-3 py-1 bg-gray-800 rounded text-xs">Artifact + Goal</div>
          <div className="text-2xl">→</div>
          <div className="px-4 py-2 bg-green-900/50 rounded-lg border border-green-600">
            <div className="text-xs text-gray-400">DIGESTOR</div>
            <div className="font-semibold">Gemini Web</div>
          </div>
          <div className="text-2xl">→</div>
          <div className="px-3 py-1 bg-gray-800 rounded text-xs">CLI Command</div>
          <div className="text-2xl">→</div>
          <div className="px-4 py-2 bg-pink-900/50 rounded-lg border border-pink-600">
            <div className="text-xs text-gray-400">EXECUTOR</div>
            <div className="font-semibold">Claude Code</div>
          </div>
        </div>
      </div>

      {/* Ground Truth */}
      <div className="mt-6 text-center">
        <div className="inline-block px-6 py-3 bg-gray-800 rounded-xl border-2 border-gray-600">
          <div className="text-xs text-gray-400 mb-1">GROUND TRUTH</div>
          <div className="font-mono text-lg">📁 Repository (Account 1 Origin)</div>
          <div className="text-xs text-gray-500 mt-1">Fingerprint: <span className="font-mono text-emerald-400">[git hash]</span></div>
        </div>
      </div>
    </div>
  );
};

export default ConstellationArchitecture;
