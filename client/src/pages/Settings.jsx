import React, { useState } from 'react';
import { CheckCircle, Key, BarChart3, Settings2, Save } from 'lucide-react';

const MODELS = [
    { id: 'gpt-4o', label: 'GPT-4o', active: true },
    { id: 'gpt-4o-mini', label: 'GPT-4o Mini' },
    { id: 'gpt-3.5', label: 'GPT-3.5' },
    { id: 'claude-3.5', label: 'Claude 3.5' },
    { id: 'gemini-pro', label: 'Gemini Pro' },
    { id: 'gemini-3.1-pro', label: 'Gemini 3.1 Pro' },
    { id: 'gemini-2.0-flash', label: 'Gemini 2.0 Flash' },
    { id: 'llama-3', label: 'Llama 3 70B' },
    { id: 'llama-3-8b', label: 'Llama 3 8B' }
];

const Settings = () => {
    const [selectedModel, setSelectedModel] = useState('gemini-2.0-flash');

    return (
        <div className="h-full w-full flex flex-col bg-[#111418] text-slate-300 font-sans p-6 overflow-y-auto">
            <div className="mb-6 flex items-center gap-2">
                <Settings2 size={24} className="text-primary" />
                <h1 className="text-xl font-bold text-white">Application Settings</h1>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div className="bg-[#161b22] border border-slate-800 rounded-lg p-6 flex flex-col">
                    <h5 className="text-sm font-semibold text-slate-300 mb-4 border-b border-slate-800 pb-2">Model Engine Configuration</h5>

                    <div className="flex flex-col gap-2 flex-1 max-h-[400px] overflow-y-auto mb-4 pr-2">
                        {MODELS.map(model => (
                            <button
                                key={model.id}
                                onClick={() => setSelectedModel(model.id)}
                                className={`
                                    w-full p-3 rounded border text-sm font-medium text-left transition-all flex items-center justify-between group
                                    ${selectedModel === model.id
                                        ? 'bg-cyan-950/30 border-cyan-500/50 text-cyan-400'
                                        : 'bg-transparent border-slate-700 text-slate-400 hover:border-slate-600 hover:text-slate-300'}
                                `}
                            >
                                {model.label}
                                {selectedModel === model.id && <CheckCircle size={16} />}
                            </button>
                        ))}
                    </div>

                    <div className="flex flex-col gap-3 mt-auto pt-4 border-t border-slate-800">
                        <button className="w-full py-2 border border-slate-700 hover:border-slate-600 rounded text-xs font-medium text-slate-400 hover:text-white flex items-center justify-center gap-2 transition-colors">
                            <Key size={14} /> Configure API Keys
                        </button>
                        <button className="w-full py-2 border border-slate-700 hover:border-slate-600 rounded text-xs font-medium text-slate-400 hover:text-white flex items-center justify-center gap-2 transition-colors">
                            <BarChart3 size={14} /> View Usage Stats
                        </button>
                        <button className="w-full py-2 bg-gradient-to-r from-cyan-600 to-cyan-500 hover:from-cyan-500 hover:to-cyan-400 text-white rounded text-xs font-bold shadow-lg flex items-center justify-center gap-2 transition-all mt-2">
                            <Save size={14} /> Save Configuration
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Settings;
