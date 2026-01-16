import React, { useState, useEffect, useRef } from 'react';
import { PanelLeftClose, PanelLeftOpen, GripVertical } from 'lucide-react';
import SearchableDropdown from '../components/SearchableDropdown';
import { DOMAIN_STRUCTURE } from '../constants/domains';

const DataCollection = () => {
    // --- Layout State ---
    const [sidebarWidth, setSidebarWidth] = useState(20); // Percentage
    const [isSidebarVisible, setIsSidebarVisible] = useState(true);
    const [isDragging, setIsDragging] = useState(false);

    // --- Selection State ---
    const [selectedDomain, setSelectedDomain] = useState(null);
    const [selectedTable, setSelectedTable] = useState(null);

    // --- Tab State ---
    const [activeTab, setActiveTab] = useState('course_general');

    const sidebarRef = useRef(null);

    // --- Resizing Logic ---
    const startResizing = (e) => {
        setIsDragging(true);
        e.preventDefault();
    };

    const stopResizing = () => {
        setIsDragging(false);
    };

    const resize = (e) => {
        if (isDragging) {
            const newWidth = (e.clientX / window.innerWidth) * 100;
            if (newWidth >= 10 && newWidth <= 50) {
                setSidebarWidth(newWidth);
            }
        }
    };

    useEffect(() => {
        window.addEventListener('mousemove', resize);
        window.addEventListener('mouseup', stopResizing);
        return () => {
            window.removeEventListener('mousemove', resize);
            window.removeEventListener('mouseup', stopResizing);
        };
    }, [isDragging]);


    // --- Handlers ---
    const handleDomainChange = (domain) => {
        setSelectedDomain(domain);
        setSelectedTable(null); // Reset table when domain changes
    };

    return (
        <div className="flex h-[calc(100vh-64px)] overflow-hidden bg-slate-50 dark:bg-[#111418] relative">

            {/* --- Left Sidebar Panel --- */}
            <div
                ref={sidebarRef}
                className={`
                    flex flex-col bg-white dark:bg-[#1e293b] border-r border-slate-200 dark:border-slate-700 transition-all duration-75 relative
                    ${!isSidebarVisible ? 'w-0 overflow-hidden' : ''}
                `}
                style={{ width: isSidebarVisible ? `${sidebarWidth}%` : '0px' }}
            >
                <div className="p-4 flex-1 flex flex-col gap-6 overflow-y-auto">
                    <div className="flex items-center justify-between">
                        <h2 className="font-bold text-lg text-slate-800 dark:text-white truncate">
                            Domain Explorer
                        </h2>
                        <button
                            onClick={() => setIsSidebarVisible(false)}
                            className="p-1 hover:bg-slate-100 dark:hover:bg-slate-700 rounded text-slate-500"
                            title="Collapse Sidebar"
                        >
                            <PanelLeftClose size={20} />
                        </button>
                    </div>

                    {/* Selection Controls */}
                    <div className="flex flex-col gap-4">
                        <SearchableDropdown
                            label="Domain"
                            placeholder="Select Domain..."
                            options={DOMAIN_STRUCTURE}
                            value={selectedDomain}
                            onChange={handleDomainChange}
                        />

                        <SearchableDropdown
                            label="Table"
                            placeholder="Select Table..."
                            options={selectedDomain ? selectedDomain.tables : []}
                            value={selectedTable}
                            onChange={setSelectedTable}
                            disabled={!selectedDomain}
                        />
                    </div>

                    {/* Data Display Area */}
                    <div className="flex-1 flex flex-col gap-2 min-h-0">
                        <label className="text-xs font-semibold text-slate-500 uppercase tracking-wider">
                            {selectedTable ? `Data: ${selectedTable.label}` : 'Data View'}
                        </label>
                        <div className="flex-1 border border-slate-200 dark:border-slate-700 rounded-lg bg-slate-50 dark:bg-[#111418] p-4 overflow-auto">
                            {selectedTable ? (
                                <div className="flex flex-col gap-2">
                                    {/* Placeholder Data List */}
                                    {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map(i => (
                                        <div key={i} className="p-2 bg-white dark:bg-[#1e293b] rounded border border-slate-100 dark:border-slate-700 text-sm hover:border-primary/50 cursor-pointer">
                                            Item {i} - {selectedTable.label} Data
                                        </div>
                                    ))}
                                </div>
                            ) : (
                                <div className="h-full flex items-center justify-center text-slate-400 text-sm text-center px-4">
                                    Select a Domain and Table to view data references.
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </div>

            {/* --- Resize Handle --- */}
            {isSidebarVisible && (
                <div
                    className="w-1 hover:w-2 bg-slate-200 dark:bg-slate-700 hover:bg-primary cursor-col-resize flex items-center justify-center z-10 transition-colors"
                    onMouseDown={startResizing}
                >
                    <div className="h-8 w-1 bg-slate-400 rounded-full" />
                </div>
            )}

            {/* --- Open Sidebar Button (when hidden) --- */}
            {!isSidebarVisible && (
                <div className="absolute left-0 top-4 z-20">
                    <button
                        onClick={() => setIsSidebarVisible(true)}
                        className="bg-white dark:bg-[#1e293b] p-2 rounded-r-md border-y border-r border-slate-200 dark:border-slate-700 shadow-md text-primary hover:text-primary/80"
                    >
                        <PanelLeftOpen size={20} />
                    </button>
                </div>
            )}

            {/* --- Right Canvas Panel --- */}
            <div className="flex-1 flex flex-col min-w-0 bg-slate-50 dark:bg-[#111418]">
                {/* Tabs Header */}
                <div className="bg-white dark:bg-[#1e293b] border-b border-slate-200 dark:border-slate-700 px-4 pt-2 flex items-center gap-1 overflow-x-auto">
                    {[
                        { id: 'course_general', label: 'Course General' },
                        { id: 'career_position', label: 'Career Position' },
                        { id: 'course_requirements', label: 'Course Requirements' },
                        { id: 'career_requirements', label: 'Career Position Requirements' }
                    ].map(tab => (
                        <button
                            key={tab.id}
                            onClick={() => setActiveTab(tab.id)}
                            className={`
                                px-4 py-3 text-sm font-medium border-b-2 transition-colors whitespace-nowrap
                                ${activeTab === tab.id
                                    ? 'border-primary text-primary'
                                    : 'border-transparent text-slate-500 hover:text-slate-700 dark:text-slate-400 dark:hover:text-slate-200'}
                            `}
                        >
                            {tab.label}
                        </button>
                    ))}
                </div>

                {/* Canvas Content */}
                <div className="flex-1 p-6 overflow-auto">
                    <div className="max-w-5xl mx-auto bg-white dark:bg-[#1e293b] rounded-xl shadow-sm border border-slate-200 dark:border-slate-700 min-h-[500px] p-8 flex flex-col items-center justify-center text-slate-400">
                        <div className="mb-4 text-6xl opacity-20 font-black tracking-tighter">
                            {activeTab.split('_').map(w => w[0].toUpperCase()).join('')}
                        </div>
                        <h3 className="text-xl font-semibold text-slate-700 dark:text-slate-200 mb-2">
                            {activeTab.split('_').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ')} Canvas
                        </h3>
                        <p className="text-center max-w-md">
                            Select a data point from the sidebar references to begin populating this form area.
                        </p>
                    </div>
                </div>
            </div>

        </div>
    );
};

export default DataCollection;
