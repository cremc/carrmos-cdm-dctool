import React, { useState } from 'react';
import { Panel, Group as PanelGroup, Separator as PanelResizeHandle } from 'react-resizable-panels';
import { GripHorizontal, CheckCircle, Play, BarChart3, Filter, Download, Key } from 'lucide-react';
import CourseGeneralForm from '../components/TabForms/CourseGeneralForm';
import CourseSpecificForm from '../components/TabForms/CourseSpecificForm';
import OthersForm from '../components/TabForms/OthersForm';
import axios from 'axios';

// --- Tab Definitions ---
const TABS = [
    { id: 'course', label: 'Course' },
    { id: 'career_position', label: 'Career Position' },
    { id: 'prerequisites', label: 'Prerequisites' },
    { id: 'skills', label: 'Skills' },
    { id: 'ets', label: 'ETs' },
    { id: 'institutions', label: 'Institutions' },
    { id: 'certifications', label: 'Certifications' },
    { id: 'core_subjects', label: 'Core Subjects' },
    { id: 'others', label: 'Others' }
];

const MODELS = [
    { id: 'gpt-4o', label: 'GPT-4o', active: true },
    { id: 'gpt-4o-mini', label: 'GPT-4o Mini' },
    { id: 'gpt-3.5', label: 'GPT-3.5' },
    { id: 'claude-3.5', label: 'Claude 3.5' },
    { id: 'gemini-pro', label: 'Gemini Pro' },
    { id: 'gemini-2.0-flash', label: 'Gemini 2.0 Flash' },
    { id: 'llama-3', label: 'Llama 3 70B' },
    { id: 'llama-3-8b', label: 'Llama 3 8B' }
];

const INITIAL_COURSE_FORM_DATA = {
    academicLevel: null,
    disciplineGroup: null,
    discipline: null,
    country: { value: 'india', label: 'India' },
    state: null,
    institutionCategory: null,
    institution: null,
    courseType: 'general', // Default to general
    selectedCheckboxes: {},
    descLength: '15 to 25 words',
    currency: 'INR',
    otherSpecs: ''
};

const COLUMN_CONFIGS = {
    general: [
        { label: '#', key: 'id', width: 'w-10' },
        { label: 'Name', key: 'name', width: 'min-w-[150px]' },
        { label: 'Description', key: 'description', width: 'min-w-[200px]' },
        { label: 'Duration', key: 'duration', width: 'min-w-[100px]' },
        { label: 'Tuition', key: 'tuition', width: 'min-w-[100px]' },
        { label: 'Rigour', key: 'rigour', width: 'min-w-[150px]' },
        { label: 'Career', key: 'career', width: 'min-w-[150px]' },
        { label: 'Group 1', key: 'group1', width: 'min-w-[150px]' },
        { label: 'Group 2', key: 'group2', width: 'min-w-[150px]' },
    ],
    specific: [
        { label: '#', key: 'id', width: 'w-10' },
        { label: 'Name', key: 'name', width: 'min-w-[150px]' },
        { label: 'Description', key: 'description', width: 'min-w-[200px]' },
        { label: 'General', key: 'course_general', width: 'min-w-[120px]' },
        { label: 'Inst Name', key: 'institution_name', width: 'min-w-[150px]' },
        { label: 'Admission', key: 'admission_criteria', width: 'min-w-[150px]' },
        { label: 'Type', key: 'course_type', width: 'min-w-[100px]' },
        { label: 'Cost', key: 'tuition_cost', width: 'min-w-[100px]' },
        { label: 'Advice', key: 'course_prep_advice', width: 'min-w-[150px]' },
        { label: 'Degree', key: 'degree_awarded', width: 'min-w-[120px]' },
        { label: 'Cert By', key: 'certified_by', width: 'min-w-[150px]' },
        { label: 'Cond By', key: 'conducted_by', width: 'min-w-[150px]' },
        { label: 'Duration', key: 'course_duration', width: 'min-w-[100px]' },
        { label: 'Career', key: 'career_prospect', width: 'min-w-[150px]' },
        { label: 'Rigour', key: 'rigour', width: 'min-w-[120px]' },
        { label: 'Active', key: 'activeness_scale', width: 'min-w-[80px]' },
        { label: 'Phys Load', key: 'physical_load_scale', width: 'min-w-[80px]' },
        { label: 'Ment Load', key: 'mental_load_scale', width: 'min-w-[80px]' },
        { label: 'Analyt Load', key: 'analytical_load_scale', width: 'min-w-[80px]' },
    ],
    others: [
        { label: '#', key: 'id', width: 'w-10' },
        { label: 'Name', key: 'name', width: 'min-w-[150px]' },
        { label: 'Description', key: 'description', width: 'min-w-[200px]' },
        { label: 'Category', key: 'category', width: 'min-w-[150px]' },
        { label: 'Details', key: 'details', width: 'min-w-[200px]' },
    ]
};

const DataCollection = () => {
    const [activeTab, setActiveTab] = useState('course');
    const [selectedModel, setSelectedModel] = useState('gemini-2.0-flash'); // Default per req
    const [results, setResults] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    // Form State
    const [courseFormData, setCourseFormData] = useState(INITIAL_COURSE_FORM_DATA);
    const [othersFormData, setOthersFormData] = useState('');

    const handleCourseFormChange = (newFormData) => {
        setCourseFormData(newFormData);
    };

    const handleResultChange = (id, field, value) => {
        setResults(prev => prev.map(row =>
            row.id === id ? { ...row, [field]: value } : row
        ));
    };

    const handleRunEngine = async () => {
        setIsLoading(true);
        try {
            let inputData = {};
            let domain = '';

            if (activeTab === 'course') {
                inputData = courseFormData;
                domain = courseFormData.courseType === 'specific' ? 'course_specific' : 'course_general';
            } else if (activeTab === 'others') {
                inputData = { query: othersFormData };
                domain = 'others';
            } else {
                console.warn("This tab is not supported for execution yet.");
                setIsLoading(false);
                return;
            }

            const response = await axios.post('http://localhost:8000/api/pe/run', {
                domain: domain,
                input_data: inputData,
                api_key: ""
            });

            if (response.data && response.data.results) {
                // Map results adding an ID if needed
                const mappedResults = response.data.results.map((item, index) => ({
                    id: String(index + 1).padStart(2, '0'),
                    ...item
                }));
                setResults(mappedResults);
            }
        } catch (error) {
            console.error("Error running engine:", error);
            alert("Failed to run engine. See console for details.");
        } finally {
            setIsLoading(false);
        }
    };

    const renderTabContent = () => {
        switch (activeTab) {
            case 'course':
                return courseFormData.courseType === 'specific'
                    ? <CourseSpecificForm formData={courseFormData} onChange={handleCourseFormChange} />
                    : <CourseGeneralForm formData={courseFormData} onChange={handleCourseFormChange} />;
            case 'others':
                return <OthersForm value={othersFormData} onChange={setOthersFormData} />;
            default:
                return (
                    <div className="h-full flex items-center justify-center text-slate-600">
                        <p>Form for {TABS.find(t => t.id === activeTab)?.label} coming soon...</p>
                    </div>
                );
        }
    };

    // get columns based on course type
    const columns = activeTab === 'course'
        ? COLUMN_CONFIGS[courseFormData.courseType] || COLUMN_CONFIGS.general
        : COLUMN_CONFIGS[activeTab] || [];

    return (
        <div className="h-[calc(100vh-64px)] w-full flex flex-col bg-[#111418] text-slate-300 overflow-hidden font-sans">

            {/* --- Horizontal Tabs --- */}
            <div className="flex items-center gap-1 overflow-x-auto border-b border-slate-800 bg-[#111418] px-4 pt-2 shrink-0 h-10 no-scrollbar">
                {TABS.map(tab => (
                    <button
                        key={tab.id}
                        onClick={() => setActiveTab(tab.id)}
                        className={`
                            px-4 py-2 text-sm font-medium transition-all relative
                            ${activeTab === tab.id
                                ? 'text-white border-b-2 border-primary'
                                : 'text-slate-500 hover:text-slate-300'}
                        `}
                    >
                        {tab.label}
                    </button>
                ))}
            </div>

            {/* --- Main Vertical Split (Top: Prompt / Bottom: Data) --- */}
            <div className="flex-1 w-full overflow-x-auto overflow-y-hidden">
                <div className="h-full min-w-[1024px]">
                    <PanelGroup orientation="vertical" className="h-full w-full">

                        {/* --- Top Panel (Prompt Config) --- */}
                        <Panel defaultSize="30" minSize="10" maxSize="50" className="flex flex-col min-h-0 bg-[#161b22]">
                            <div className="flex-1 flex flex-col p-4 pb-0 min-h-0">
                                <div className="flex items-center gap-2 mb-2 shrink-0">
                                    <div className="text-primary"><BarChart3 size={16} /></div>
                                    <h3 className="text-sm font-semibold text-slate-400">Prompt configuration</h3>

                                    {/* Course Type Switch */}
                                    {activeTab === 'course' && (
                                        <div className="flex bg-[#111418] rounded p-0.5 border border-slate-800 ml-4">
                                            <button
                                                className={`px-3 py-0.5 text-[10px] font-medium rounded-sm transition-colors ${courseFormData.courseType !== 'specific' ? 'bg-slate-700 text-white' : 'text-slate-500 hover:text-slate-300'}`}
                                                onClick={() => handleCourseFormChange({ ...courseFormData, courseType: 'general' })}
                                            >
                                                Course Gen
                                            </button>
                                            <button
                                                className={`px-3 py-0.5 text-[10px] font-medium rounded-sm transition-colors ${courseFormData.courseType === 'specific' ? 'bg-slate-700 text-white' : 'text-slate-500 hover:text-slate-300'}`}
                                                onClick={() => handleCourseFormChange({ ...courseFormData, courseType: 'specific' })}
                                            >
                                                Course Spec
                                            </button>
                                        </div>
                                    )}

                                </div>

                                {/* --- Horizontal Split (Left: form / Right: Selection) --- */}
                                <div className="flex-1 min-h-0 border border-slate-800/50 rounded-lg bg-[#161b22] overflow-hidden">
                                    <PanelGroup orientation="horizontal" className="h-full w-full">
                                        {/* Left: Dynamic Form */}
                                        <Panel defaultSize="80" minSize="50" className="p-4 relative min-w-[300px]">
                                            <div className="h-full overflow-auto overflow-x-auto text-sm">
                                                {renderTabContent()}
                                            </div>

                                            {/* Action Buttons (Absolute Bottom Right of Left Panel) */}
                                            <div className="absolute bottom-4 right-4 flex gap-2 z-10">
                                                <button
                                                    onClick={() => setResults([])}
                                                    className="px-3 py-1.5 border border-slate-700 hover:border-slate-500 text-slate-400 hover:text-white rounded text-xs font-medium transition-colors bg-[#161b22]"
                                                >
                                                    Clear
                                                </button>
                                                <button
                                                    onClick={() => {
                                                        if (results.length === 0) return;
                                                        const headers = columns.map(c => c.label).join('\t');
                                                        const rows = results.map(r => columns.map(c => r[c.key] || '').join('\t')).join('\n');
                                                        navigator.clipboard.writeText(`${headers}\n${rows}`);
                                                        alert('Data copied to clipboard!');
                                                    }}
                                                    className="px-3 py-1.5 border border-slate-700 hover:border-slate-500 text-slate-400 hover:text-white rounded text-xs font-medium transition-colors bg-[#161b22]"
                                                >
                                                    Copy
                                                </button>
                                                <button
                                                    onClick={handleRunEngine}
                                                    disabled={isLoading}
                                                    className="px-4 py-1.5 bg-gradient-to-r from-cyan-600 to-cyan-500 hover:from-cyan-500 hover:to-cyan-400 text-white rounded text-xs font-bold shadow-lg shadow-cyan-900/20 flex items-center gap-1.5 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                                                >
                                                    <Play size={12} fill="currentColor" />
                                                    {isLoading ? 'Running...' : 'Run engine'}
                                                </button>
                                            </div>
                                        </Panel>

                                        <PanelResizeHandle className="w-1 bg-slate-800 hover:bg-primary transition-colors cursor-col-resize flex items-center justify-center">
                                            <div className="w-0.5 h-8 bg-slate-600 rounded-full" />
                                        </PanelResizeHandle>

                                        {/* Right: Selection Panel */}
                                        <Panel defaultSize="20" minSize="15" className="bg-[#111418] border-l border-slate-800 flex flex-col">
                                            <div className="p-3 flex flex-col h-full">
                                                <h5 className="text-xs font-semibold text-slate-400 mb-2">Model engine</h5>

                                                <div className="flex flex-col gap-2 flex-1 overflow-y-auto">
                                                    {MODELS.map(model => (
                                                        <button
                                                            key={model.id}
                                                            onClick={() => setSelectedModel(model.id)}
                                                            className={`
                                                        w-full p-2.5 rounded border text-xs font-medium text-left transition-all flex items-center justify-between group
                                                        ${selectedModel === model.id
                                                                    ? 'bg-cyan-950/30 border-cyan-500/50 text-cyan-400'
                                                                    : 'bg-transparent border-slate-700 text-slate-400 hover:border-slate-600 hover:text-slate-300'}
                                                    `}
                                                        >
                                                            {model.label}
                                                            {selectedModel === model.id && <CheckCircle size={14} />}
                                                        </button>
                                                    ))}
                                                </div>

                                                <div className="flex flex-col gap-2 mt-auto pt-2">
                                                    <button className="w-full py-1.5 border border-slate-700 hover:border-slate-600 rounded text-[10px] font-medium text-slate-500 hover:text-slate-300 flex items-center justify-center gap-2 transition-colors">
                                                        <Key size={12} /> API keys
                                                    </button>
                                                    <button className="w-full py-1.5 border border-slate-700 hover:border-slate-600 rounded text-[10px] font-medium text-slate-500 hover:text-slate-300 flex items-center justify-center gap-2 transition-colors">
                                                        <BarChart3 size={12} /> Usage
                                                    </button>
                                                </div>
                                            </div>
                                        </Panel>
                                    </PanelGroup>
                                </div>
                            </div>
                        </Panel>

                        {/* --- Divider --- */}
                        <PanelResizeHandle className="h-2 bg-[#111418] flex items-center justify-center hover:bg-slate-800 transition-colors cursor-row-resize relative z-50 border-y border-slate-800">
                            <div className="w-16 h-1 bg-slate-700 rounded-full pointer-events-none" />
                        </PanelResizeHandle>

                        {/* --- Bottom Panel (Data) --- */}
                        <Panel minSize="20" className="flex flex-col bg-[#161b22] min-h-0">
                            <div className="flex items-center justify-between px-6 py-2 border-b border-slate-800 shrink-0">
                                <div className="flex items-center gap-3">
                                    <div className="text-cyan-500"><BarChart3 size={18} /></div>
                                    <h3 className="text-sm font-semibold text-slate-400 flex items-center gap-2">
                                        Generated output
                                        <span className="px-2 py-0.5 rounded-full bg-cyan-950 text-cyan-500 text-[10px]">{results.length} Result(s)</span>
                                    </h3>
                                </div>
                                <div className="flex items-center gap-4">
                                    <button className="text-[10px] font-medium text-slate-500 hover:text-slate-300 flex items-center gap-1">
                                        <Filter size={12} /> Filter
                                    </button>
                                    <button className="text-[10px] font-medium text-slate-500 hover:text-slate-300 flex items-center gap-1">
                                        <Download size={12} /> Export
                                    </button>
                                </div>
                            </div>

                            {/* Data Table Area */}
                            <div className="flex-1 overflow-auto overflow-x-auto p-0 scrollbar-thin scrollbar-thumb-slate-700 scrollbar-track-slate-900">
                                <table className="w-full text-left border-collapse">
                                    <thead className="sticky top-0 bg-[#161b22] z-10 text-[10px] font-bold text-slate-500 border-b border-slate-800 shadow-sm">
                                        <tr>
                                            {columns.map(col => (
                                                <th key={col.key} className={`p-3 text-left ${col.width}`}>{col.label}</th>
                                            ))}
                                            <th className="p-3 text-right">Actions</th>
                                        </tr>
                                    </thead>
                                    <tbody className="text-xs text-slate-300">
                                        {results.map((row) => (
                                            <tr key={row.id} className="border-b border-slate-800/50 hover:bg-slate-800/30 transition-colors group">
                                                {columns.map(col => (
                                                    <td key={col.key} className="p-3">
                                                        {/* Using inputs for editing capabilities */}
                                                        <textarea
                                                            value={row[col.key] || ''}
                                                            onChange={(e) => handleResultChange(row.id, col.key, e.target.value)}
                                                            className="w-full bg-transparent border-none focus:outline-none focus:ring-1 focus:ring-primary rounded px-1 py-0.5 hover:bg-slate-800/50 min-h-[24px] resize-none overflow-hidden text-ellipsis text-nowrap focus:text-wrap focus:h-auto z-10 relative"
                                                            rows={1}
                                                        />
                                                    </td>
                                                ))}
                                                <td className="p-3 text-right">
                                                    <button className="text-slate-600 hover:text-white transition-colors p-1"><GripHorizontal size={14} /></button>
                                                </td>
                                            </tr>
                                        ))}
                                        {results.length === 0 && (
                                            <tr>
                                                <td colSpan={columns.length + 1} className="p-8 text-center text-slate-600 italic">
                                                    No results generated yet. Configure and run the engine.
                                                </td>
                                            </tr>
                                        )}
                                    </tbody>
                                </table>
                            </div>

                            {/* Bottom Action Bar */}
                            <div className="shrink-0 p-3 border-t border-slate-800 flex justify-end gap-3 bg-[#161b22]">
                                <button
                                    className="px-3 py-1.5 border border-slate-700 hover:border-slate-500 text-slate-400 hover:text-white rounded text-xs font-medium transition-colors"
                                    onClick={() => setResults([])}
                                >
                                    Clear board
                                </button>
                                <button
                                    onClick={() => {
                                        if (results.length === 0) return;
                                        const headers = columns.map(c => c.label).join('\t');
                                        const rows = results.map(r => columns.map(c => r[c.key] || '').join('\t')).join('\n');
                                        navigator.clipboard.writeText(`${headers}\n${rows}`);
                                        alert('Data copied to clipboard!');
                                    }}
                                    className="px-3 py-1.5 border border-slate-700 hover:border-slate-500 text-slate-400 hover:text-white rounded text-xs font-medium transition-colors"
                                >
                                    Copy batch
                                </button>
                                <button className="px-4 py-1.5 bg-white text-slate-900 hover:bg-slate-200 rounded text-xs font-bold shadow-lg flex items-center gap-2 transition-all">
                                    <Download size={14} />
                                    Push to staging
                                </button>
                            </div>
                        </Panel>
                    </PanelGroup>
                </div>
            </div>

        </div>
    );
};

export default DataCollection;
