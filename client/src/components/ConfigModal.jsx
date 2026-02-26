import React from 'react';
import { X, Save } from 'lucide-react';

const ConfigModal = ({ isOpen, onClose, onSave, headerContent, setHeaderContent, footerContent, setFooterContent }) => {
    if (!isOpen) return null;

    return (
        <div className="fixed inset-0 z-[100] flex items-center justify-center bg-black/50 backdrop-blur-sm">
            <div className="bg-[#161b22] border border-slate-700 w-[700px] h-[600px] rounded-lg shadow-2xl flex flex-col overflow-hidden">
                <div className="flex items-center justify-between px-4 py-3 border-b border-slate-800 bg-[#111418]">
                    <h3 className="text-sm font-semibold text-slate-300">Configure Prompt Header & Footer</h3>
                    <button onClick={onClose} className="text-slate-500 hover:text-white transition-colors">
                        <X size={18} />
                    </button>
                </div>
                <div className="flex-1 p-4 overflow-y-auto flex flex-col gap-4">
                    <div className="flex flex-col gap-2 h-1/3">
                        <label className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Prompt Header</label>
                        <textarea
                            className="w-full flex-1 bg-[#0d1117] border border-slate-800 rounded p-3 text-sm font-mono text-slate-300 focus:outline-none focus:border-primary resize-none"
                            value={headerContent}
                            onChange={(e) => setHeaderContent(e.target.value)}
                            placeholder="Enter prompt header..."
                        ></textarea>
                    </div>
                    <div className="flex flex-col gap-2 flex-1">
                        <label className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Prompt Footer</label>
                        <textarea
                            className="w-full flex-1 bg-[#0d1117] border border-slate-800 rounded p-3 text-sm font-mono text-slate-300 focus:outline-none focus:border-primary resize-none"
                            value={footerContent}
                            onChange={(e) => setFooterContent(e.target.value)}
                            placeholder="Enter prompt footer..."
                        ></textarea>
                    </div>
                </div>
                <div className="px-4 py-3 border-t border-slate-800 bg-[#111418] flex justify-end gap-3 shrink-0">
                    <button onClick={onClose} className="px-4 py-1.5 border border-slate-700 hover:border-slate-500 text-slate-400 hover:text-white rounded text-xs font-medium transition-colors">
                        Cancel
                    </button>
                    <button onClick={() => { onSave(); onClose(); }} className="px-4 py-1.5 bg-gradient-to-r from-cyan-600 to-cyan-500 hover:from-cyan-500 hover:to-cyan-400 text-white flex items-center gap-2 rounded text-xs font-bold shadow-lg transition-all">
                        <Save size={14} />
                        Save
                    </button>
                </div>
            </div>
        </div>
    );
};

export default ConfigModal;
