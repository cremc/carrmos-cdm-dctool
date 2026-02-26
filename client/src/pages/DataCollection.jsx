import React, { useState, useRef } from 'react';
import { Panel, Group as PanelGroup, Separator as PanelResizeHandle } from 'react-resizable-panels';
import { GripHorizontal, CheckCircle, Play, BarChart3, Filter, Download, Key, Edit2, Settings2 } from 'lucide-react';
import NotepadModal from '../components/NotepadModal';
import ConfigModal from '../components/ConfigModal';
import CourseGeneralForm from '../components/TabForms/CourseGeneralForm';
import CourseSpecificForm from '../components/TabForms/CourseSpecificForm';
import CareerPositionForm from '../components/TabForms/CareerPositionForm';
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

const INITIAL_CAREER_POSITION_FORM_DATA = {
    industry: null,
    industryBranch: null,
    roleType: null,
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
    career_position: [
        { label: '#', key: 'id', width: 'w-10' },
        { label: 'Name', key: 'name', width: 'min-w-[150px]' },
        { label: 'Description', key: 'description', width: 'min-w-[200px]' },
        { label: 'Industry', key: 'industry', width: 'min-w-[150px]' },
        { label: 'Branch', key: 'industry_branch', width: 'min-w-[150px]' },
        { label: 'Salary', key: 'salary_range', width: 'min-w-[120px]' },
        { label: 'Employers', key: 'employing_organizations', width: 'min-w-[200px]' },
        { label: 'Growth', key: 'career_growth_potential', width: 'min-w-[100px]' },
        { label: 'Stability', key: 'job_stability_potential', width: 'min-w-[100px]' },
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
    const [dynamicColumns, setDynamicColumns] = useState([]);

    const [isEditPromptOpen, setIsEditPromptOpen] = useState(false);
    const [isPromptHeaderOpen, setIsPromptHeaderOpen] = useState(false);
    const [editPromptContent, setEditPromptContent] = useState('');
    const [promptHeaderContent, setPromptHeaderContent] = useState('');
    const [promptFooterContent, setPromptFooterContent] = useState('');

    const topPanelRef = useRef(null);

    // Form State
    const [courseFormData, setCourseFormData] = useState(INITIAL_COURSE_FORM_DATA);
    const [careerPositionFormData, setCareerPositionFormData] = useState(INITIAL_CAREER_POSITION_FORM_DATA);
    const [othersFormData, setOthersFormData] = useState('');

    const handleCourseFormChange = (newFormData) => {
        setCourseFormData(newFormData);
    };

    const handleCareerPositionFormChange = (newFormData) => {
        setCareerPositionFormData(newFormData);
    };

    const handleResultChange = (id, field, value) => {
        setResults(prev => prev.map(row =>
            row.id === id ? { ...row, [field]: value } : row
        ));
    };

    const handleClear = () => {
        if (activeTab === 'course') {
            setCourseFormData({
                ...INITIAL_COURSE_FORM_DATA,
                country: { value: 'india', label: 'India' }
            });
        } else if (activeTab === 'career_position') {
            setCareerPositionFormData(INITIAL_CAREER_POSITION_FORM_DATA);
        } else if (activeTab === 'others') {
            setOthersFormData('');
        }
    };

    const handleRunEngine = async () => {
        setIsLoading(true);
        try {
            let inputData = {};
            let domain = '';

            if (activeTab === 'course') {
                inputData = courseFormData;
                domain = courseFormData.courseType === 'specific' ? 'course_specific' : 'course_general';
            } else if (activeTab === 'career_position') {
                inputData = careerPositionFormData;
                domain = 'career_position';
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

                // If Others tab, generate dynamic columns from first result
                if (activeTab === 'others' && mappedResults.length > 0) {
                    const firstItem = mappedResults[0];
                    const newCols = Object.keys(firstItem)
                        .filter(key => key !== 'id') // exclude ID as we handle it separately
                        .map(key => ({
                            label: key.charAt(0).toUpperCase() + key.slice(1).replace(/_/g, ' '),
                            key: key,
                            width: 'min-w-[150px]'
                        }));
                    // Always prepend ID column
                    setDynamicColumns([
                        { label: '#', key: 'id', width: 'w-10' },
                        ...newCols
                    ]);
                }
            }
        } catch (error) {
            console.error("Error running engine:", error);
            alert("Failed to run engine. See console for details.");
        } finally {
            setIsLoading(false);
        }
    };

    const handleFocusSpecs = () => {
        if (topPanelRef.current) {
            topPanelRef.current.resize(80);
        }
    };

    const handleOpenPreview = async () => {
        setIsLoading(true);
        try {
            let inputData = {};
            let domain = '';
            if (activeTab === 'course') {
                inputData = courseFormData;
                domain = courseFormData.courseType === 'specific' ? 'course_specific' : 'course_general';
            } else if (activeTab === 'career_position') {
                inputData = careerPositionFormData;
                domain = 'career_position';
            } else if (activeTab === 'others') {
                inputData = { query: othersFormData };
                domain = 'others';
            }

            const res = await axios.post('http://localhost:8000/api/pe/preview', {
                domain,
                input_data: inputData
            });
            setEditPromptContent(res.data.prompt);
            setIsEditPromptOpen(true);
        } catch (e) {
            console.error("Preview error:", e);
            alert("Failed to fetch prompt preview.");
        } finally {
            setIsLoading(false);
        }
    };

    const handleOpenConfig = async () => {
        try {
            const res = await axios.get('http://localhost:8000/api/pe/config');
            setPromptHeaderContent(res.data.header || '');
            setPromptFooterContent(res.data.footer || '');
            setIsPromptHeaderOpen(true);
        } catch (e) {
            console.error("Config fetch error:", e);
            alert("Failed to fetch config.");
        }
    };

    const handleSaveConfig = async (content) => {
        // Here we just save the config using an endpoint
        // Because NotepadModal only gives one 'content', we'll split it or just save the header for now if we didn't update NotepadModal to have two fields.
        // Or we can just join them and send to backend.
        // Let's assume content acts as header for now, or the user edits the entire thing.
        try {
            await axios.post('http://localhost:8000/api/pe/config', {
                header: content,
                footer: promptFooterContent // keep existing footer if NotepadModal only edits one string
            });
            setPromptHeaderContent(content);
        } catch (e) {
            console.error("Save config error:", e);
        }
    };

    const renderActionButtons = () => (
        <div className="flex justify-between z-10 w-full mt-4">
            {/* Bottom Left Corner Icons */}
            <div className="flex gap-2">
                <button
                    onClick={handleOpenPreview}
                    className="p-2 border border-slate-700 hover:border-slate-500 text-slate-400 hover:text-white rounded transition-colors bg-[#161b22]" title="Preview Prompt">
                    <Edit2 size={16} />
                </button>
                <button
                    onClick={handleOpenConfig}
                    className="p-2 border border-slate-700 hover:border-slate-500 text-slate-400 hover:text-white rounded transition-colors bg-[#161b22]" title="Prompt Header">
                    <Settings2 size={16} />
                </button>
            </div>

            {/* Bottom Right Corner Buttons */}
            <div className="flex gap-2">
                <button
                    onClick={handleClear}
                    className="px-3 py-1.5 border border-slate-700 hover:border-slate-500 text-slate-400 hover:text-white rounded text-xs font-medium transition-colors bg-[#161b22]"
                >
                    Clear
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
        </div>
    );

    const renderTabContent = () => {
        switch (activeTab) {
            case 'course':
                return courseFormData.courseType === 'specific'
                    ? <CourseSpecificForm formData={courseFormData} onChange={handleCourseFormChange} renderActionButtons={renderActionButtons} onFocusSpecs={handleFocusSpecs} />
                    : <CourseGeneralForm formData={courseFormData} onChange={handleCourseFormChange} renderActionButtons={renderActionButtons} onFocusSpecs={handleFocusSpecs} />;
            case 'career_position':
                return <CareerPositionForm formData={careerPositionFormData} onChange={handleCareerPositionFormChange} renderActionButtons={renderActionButtons} onFocusSpecs={handleFocusSpecs} />;
            case 'others':
                return <OthersForm value={othersFormData} onChange={setOthersFormData} renderActionButtons={renderActionButtons} onFocusSpecs={handleFocusSpecs} />;
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
        : activeTab === 'others' && dynamicColumns.length > 0
            ? dynamicColumns
            : COLUMN_CONFIGS[activeTab] || [];

    return (
        <div className="h-full w-full flex flex-col bg-[#111418] text-slate-300 overflow-hidden font-sans">

            {/* --- Horizontal Tabs --- */}
            <div className="flex items-center border-b border-slate-800 bg-[#111418] px-0 pt-0 shrink-0 h-10 w-full">
                {TABS.map(tab => (
                    <button
                        key={tab.id}
                        onClick={() => setActiveTab(tab.id)}
                        className={`
                            px-2 py-2 text-xs font-medium transition-all relative flex-1 justify-center h-full border-r border-[#1e2329] last:border-r-0
                            ${activeTab === tab.id
                                ? 'text-white border-b-2 border-b-primary bg-[#161b22]'
                                : 'text-slate-500 hover:text-slate-300 hover:bg-[#161b22]/50'}
                        `}
                    >
                        {tab.label}
                    </button>
                ))}
            </div>

            {/* --- Main Vertical Split (Top: Prompt / Bottom: Data) --- */}
            <div className="flex-1 w-full overflow-x-auto overflow-y-hidden">
                <div className="h-full min-w-[1300px] flex flex-col">
                    <PanelGroup orientation="vertical" className="flex-1">

                        {/* --- Top Panel (Prompt Config) --- */}
                        <Panel ref={topPanelRef} defaultSize="30" minSize="10" maxSize="80" className="flex flex-col min-h-0 bg-[#161b22]">
                            <div className="flex-1 flex flex-col p-4 pb-0 min-h-0">
                                <div className="flex items-center justify-between mb-2 shrink-0 relative">
                                    <div className="flex items-center gap-2">
                                        <div className="text-primary"><BarChart3 size={16} /></div>
                                        <h3 className="text-sm font-semibold text-slate-400">Prompt configuration</h3>
                                    </div>

                                    {/* Course Type Switch - Centered */}
                                    {activeTab === 'course' && (
                                        <div className="absolute left-1/2 -translate-x-1/2 flex bg-[#111418] rounded p-0.5 border border-slate-800">
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

                                    {/* Spacer to balance the flex layout if needed, or keeping empty for now */}
                                    <div className="w-[100px]"></div>
                                </div>

                                {/* --- Form Area --- */}
                                <div className="flex-1 min-h-0 border border-slate-800/50 rounded-lg bg-[#161b22] overflow-hidden relative p-4">
                                    <div className="h-full overflow-auto overflow-x-auto text-sm">
                                        {renderTabContent()}
                                    </div>
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
                            <div className="flex-1 overflow-auto p-0 scrollbar-thin scrollbar-thumb-slate-700 scrollbar-track-slate-900">
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

            <NotepadModal
                isOpen={isEditPromptOpen}
                onClose={() => setIsEditPromptOpen(false)}
                onSave={(content) => { setEditPromptContent(content); console.log("Saved edit prompt", content); }}
                title="Edit Engineered Prompt"
                content={editPromptContent}
                setContent={setEditPromptContent}
            />

            <ConfigModal
                isOpen={isPromptHeaderOpen}
                onClose={() => setIsPromptHeaderOpen(false)}
                onSave={() => handleSaveConfig(promptHeaderContent)}
                headerContent={promptHeaderContent}
                setHeaderContent={setPromptHeaderContent}
                footerContent={promptFooterContent}
                setFooterContent={setPromptFooterContent}
            />

        </div>
    );
};

export default DataCollection;
