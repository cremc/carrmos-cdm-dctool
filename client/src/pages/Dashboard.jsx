import React from 'react';


import {
    Clock,
    BellRing,
    CalendarX2,
    ListFilter,
    MoreVertical as MoreVert,
    Play,
    CheckCircle2,
    PlusCircle,
    History as HistoryIcon,
    ClipboardCheck,
    Calendar,
    MessageSquare,
    FolderInput,
    AlertTriangle
} from 'lucide-react';

import { useNavigate } from 'react-router-dom';

const Dashboard = () => {
    const navigate = useNavigate();
    return (
        <div className="flex-1 flex flex-col items-center py-6 px-4 md:px-8 lg:px-10 w-full">
            <div className="w-full max-w-7xl flex flex-col gap-6">

                {/* Welcome Section */}
                <div className="flex flex-col gap-6">
                    <div className="flex flex-col md:flex-row md:items-end justify-between gap-4">
                        <div className="flex flex-col gap-2">
                            <h1 className="text-slate-900 dark:text-white text-3xl md:text-4xl font-black leading-tight tracking-[-0.033em]">
                                Welcome back, Ankur
                            </h1>
                            <p className="text-slate-500 dark:text-[#9dabb8] text-base font-normal leading-normal">
                                Here is an overview of your data collection activities for this semester.
                            </p>
                        </div>
                    </div>

                    {/* Stats Grid */}
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div className="flex flex-col gap-2 rounded-xl p-5 border border-gray-200 dark:border-[#3c4753] bg-white dark:bg-[#1e293b] shadow-sm">
                            <div className="flex items-center justify-between">
                                <p className="text-slate-500 dark:text-[#9dabb8] text-sm font-medium uppercase tracking-wider">Pending Tasks</p>
                                <Clock className="text-primary" size={24} />
                            </div>
                            <p className="text-slate-900 dark:text-white tracking-tight text-3xl font-bold leading-tight">3</p>
                        </div>
                        <div className="flex flex-col gap-2 rounded-xl p-5 border border-gray-200 dark:border-[#3c4753] bg-white dark:bg-[#1e293b] shadow-sm">
                            <div className="flex items-center justify-between">
                                <p className="text-slate-500 dark:text-[#9dabb8] text-sm font-medium uppercase tracking-wider">New Notifications</p>
                                <BellRing className="text-amber-500" size={24} />
                            </div>
                            <p className="text-slate-900 dark:text-white tracking-tight text-3xl font-bold leading-tight">5</p>
                        </div>
                        <div className="flex flex-col gap-2 rounded-xl p-5 border border-gray-200 dark:border-[#3c4753] bg-white dark:bg-[#1e293b] shadow-sm">
                            <div className="flex items-center justify-between">
                                <p className="text-slate-500 dark:text-[#9dabb8] text-sm font-medium uppercase tracking-wider">Upcoming Deadlines</p>
                                <CalendarX2 className="text-rose-500" size={24} />
                            </div>
                            <p className="text-slate-900 dark:text-white tracking-tight text-3xl font-bold leading-tight">2</p>
                        </div>
                    </div>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 mt-2">
                    {/* Main Tasks Column */}
                    <section className="lg:col-span-6 flex flex-col gap-4">
                        <div className="flex items-center justify-between">
                            <h2 className="text-slate-900 dark:text-white text-xl font-bold">Current User Tasks</h2>
                            <div className="flex gap-2">
                                <button className="flex h-8 items-center gap-x-1 rounded-lg bg-slate-100 dark:bg-[#293038] pl-3 pr-2 transition-colors hover:bg-slate-200 dark:hover:bg-[#363f4a]">
                                    <span className="text-slate-700 dark:text-white text-xs font-medium">Filter</span>
                                    <ListFilter className="text-slate-700 dark:text-white" size={18} />
                                </button>
                            </div>
                        </div>
                        <div className="flex flex-col gap-4">
                            {/* Task Card 1 */}
                            <div className="flex flex-col gap-4 rounded-xl p-5 border border-gray-200 dark:border-[#3c4753] bg-white dark:bg-[#1e293b] shadow-sm hover:border-primary/50 transition-colors group">
                                <div className="flex justify-between items-start">
                                    <div className="flex flex-col">
                                        <div className="flex items-center gap-2 mb-1">
                                            <span className="px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wide bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-300">In Progress</span>
                                            <span className="text-xs text-slate-400 dark:text-slate-500">Last updated 2h ago</span>
                                        </div>
                                        <h3 className="text-lg font-bold text-slate-900 dark:text-white group-hover:text-primary transition-colors">Course Ranking Review</h3>
                                        <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">Review and update ranking data for engineering courses.</p>
                                    </div>
                                    <button className="text-slate-400 hover:text-slate-600 dark:hover:text-white transition-colors">
                                        <MoreVert size={20} />
                                    </button>
                                </div>
                                <div className="flex flex-col gap-2">
                                    <div className="flex justify-between text-xs font-medium">
                                        <span className="text-slate-600 dark:text-slate-300">Progress</span>
                                        <span className="text-primary">60%</span>
                                    </div>
                                    <div className="h-2 w-full bg-slate-100 dark:bg-slate-700 rounded-full overflow-hidden">
                                        <div className="h-full bg-primary w-[60%] rounded-full"></div>
                                    </div>
                                </div>
                                <div className="pt-2 flex justify-end">
                                    <button className="bg-primary/10 hover:bg-primary/20 text-primary px-4 py-2 rounded-lg text-sm font-semibold transition-colors">
                                        Continue
                                    </button>
                                </div>
                            </div>

                            {/* Task Card 2 */}
                            <div className="flex flex-col gap-4 rounded-xl p-5 border border-gray-200 dark:border-[#3c4753] bg-white dark:bg-[#1e293b] shadow-sm hover:border-primary/50 transition-colors group">
                                <div className="flex justify-between items-start">
                                    <div className="flex flex-col">
                                        <div className="flex items-center gap-2 mb-1">
                                            <span className="px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wide bg-slate-100 text-slate-600 dark:bg-slate-700 dark:text-slate-300">Not Started</span>
                                        </div>
                                        <h3 className="text-lg font-bold text-slate-900 dark:text-white group-hover:text-primary transition-colors">Institution Contact Update</h3>
                                        <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">Update placement officer details for IIT Bombay.</p>
                                    </div>
                                    <button className="text-slate-400 hover:text-slate-600 dark:hover:text-white transition-colors">
                                        <MoreVert size={20} />
                                    </button>
                                </div>
                                <div className="flex flex-col gap-2">
                                    <div className="flex justify-between text-xs font-medium">
                                        <span className="text-slate-600 dark:text-slate-300">Progress</span>
                                        <span className="text-slate-400">0%</span>
                                    </div>
                                    <div className="h-2 w-full bg-slate-100 dark:bg-slate-700 rounded-full overflow-hidden">
                                        <div className="h-full bg-slate-400 w-[0%] rounded-full"></div>
                                    </div>
                                </div>
                                <div className="pt-2 flex justify-end">
                                    <button className="bg-primary hover:bg-primary/90 text-white px-4 py-2 rounded-lg text-sm font-semibold transition-colors shadow-lg shadow-primary/20">
                                        Start Task
                                    </button>
                                </div>
                            </div>

                            {/* Task Card 3 */}
                            <div className="flex flex-col gap-4 rounded-xl p-5 border border-gray-200 dark:border-[#3c4753] bg-white dark:bg-[#1e293b] shadow-sm opacity-70 hover:opacity-100 transition-opacity">
                                <div className="flex justify-between items-start">
                                    <div className="flex flex-col">
                                        <div className="flex items-center gap-2 mb-1">
                                            <span className="px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wide bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-300">Submitted</span>
                                        </div>
                                        <h3 className="text-lg font-bold text-slate-900 dark:text-white">Placement Report Verification</h3>
                                    </div>
                                    <CheckCircle2 className="text-green-500" size={24} />
                                </div>
                                <div className="flex flex-col gap-2">
                                    <div className="flex justify-between text-xs font-medium">
                                        <span className="text-slate-600 dark:text-slate-300">Status</span>
                                        <span className="text-green-500">Complete</span>
                                    </div>
                                    <div className="h-2 w-full bg-slate-100 dark:bg-slate-700 rounded-full overflow-hidden">
                                        <div className="h-full bg-green-500 w-[100%] rounded-full"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    {/* Right Columns (Notifications & Deadlines) */}
                    <div className="lg:col-span-6 grid grid-cols-1 md:grid-cols-2 gap-6">
                        {/* Notifications */}
                        <section className="flex flex-col gap-4">
                            <div className="flex items-center justify-between">
                                <h2 className="text-slate-900 dark:text-white text-xl font-bold">Notifications</h2>
                                <button className="text-primary text-xs font-semibold hover:underline">Mark all read</button>
                            </div>
                            <div className="flex flex-col rounded-xl border border-gray-200 dark:border-[#3c4753] bg-white dark:bg-[#1e293b] shadow-sm divide-y divide-gray-100 dark:divide-[#293038] overflow-hidden">
                                {[
                                    { icon: <div className="size-2 rounded-full bg-primary mb-1 ml-1"></div>, title: "Ranking Data Verified", desc: 'Your "Top 50 MBA" list has been verified.', time: "10 mins ago" },
                                    { icon: <AlertTriangle className="text-amber-500" size={20} />, title: "Platform Update", desc: "New career mapping tools available this Friday.", time: "2 hours ago" },
                                    { icon: <MessageSquare className="text-slate-400" size={20} />, title: "Feedback on Profile", desc: 'Admin commented on "BITS Pilani Profile".', time: "Yesterday" },
                                    { icon: <FolderInput className="text-slate-400" size={20} />, title: "New Project Assigned", desc: 'You have been added to "Placement 2024" project.', time: "2 days ago" }
                                ].map((item, i) => (
                                    <div key={i} className="p-4 flex gap-3 hover:bg-slate-50 dark:hover:bg-[#252f3e] transition-colors cursor-pointer group">
                                        <div className="mt-1 min-w-[24px]">
                                            {item.icon}
                                        </div>
                                        <div className="flex flex-col gap-1">
                                            <p className="text-sm font-semibold text-slate-900 dark:text-white leading-tight group-hover:text-primary transition-colors">{item.title}</p>
                                            <p className="text-xs text-slate-500 dark:text-slate-400">{item.desc}</p>
                                            <p className="text-[10px] text-slate-400 mt-1">{item.time}</p>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </section>

                        {/* Deadlines */}
                        <section className="flex flex-col gap-4">
                            <div className="flex items-center justify-between">
                                <h2 className="text-slate-900 dark:text-white text-xl font-bold">Deadlines</h2>
                                <button className="flex h-8 items-center justify-center rounded-lg bg-slate-100 dark:bg-[#293038] px-2 transition-colors hover:bg-slate-200 dark:hover:bg-[#363f4a]">
                                    <Calendar className="text-slate-700 dark:text-white" size={18} />
                                </button>
                            </div>
                            <div className="flex flex-col gap-3">
                                {/* Deadline 1 */}
                                <div className="relative flex flex-col gap-2 rounded-xl bg-white dark:bg-[#1e293b] p-4 border border-rose-200 dark:border-rose-900/30 shadow-sm overflow-hidden">
                                    <div className="absolute left-0 top-0 bottom-0 w-1 bg-rose-500"></div>
                                    <div className="flex justify-between items-start pl-2">
                                        <div className="flex flex-col">
                                            <p className="text-xs font-bold text-rose-600 dark:text-rose-400 uppercase tracking-wide mb-1">Due in 2 Days</p>
                                            <h4 className="text-sm font-bold text-slate-900 dark:text-white">Scholarship Data Review</h4>
                                        </div>
                                        <div className="flex flex-col items-center bg-slate-50 dark:bg-[#111418] rounded p-1 min-w-[40px]">
                                            <span className="text-[10px] uppercase font-bold text-slate-500">Oct</span>
                                            <span className="text-lg font-bold text-slate-900 dark:text-white leading-none">24</span>
                                        </div>
                                    </div>
                                    <p className="text-xs text-slate-500 pl-2">Assigned by <span className="text-slate-700 dark:text-slate-300 font-medium">Data Manager</span></p>
                                </div>

                                {/* Deadline 2 */}
                                <div className="relative flex flex-col gap-2 rounded-xl bg-white dark:bg-[#1e293b] p-4 border border-gray-200 dark:border-[#3c4753] shadow-sm overflow-hidden">
                                    <div className="absolute left-0 top-0 bottom-0 w-1 bg-primary"></div>
                                    <div className="flex justify-between items-start pl-2">
                                        <div className="flex flex-col">
                                            <p className="text-xs font-bold text-primary uppercase tracking-wide mb-1">Due Next Week</p>
                                            <h4 className="text-sm font-bold text-slate-900 dark:text-white">Corporate Partner List</h4>
                                        </div>
                                        <div className="flex flex-col items-center bg-slate-50 dark:bg-[#111418] rounded p-1 min-w-[40px]">
                                            <span className="text-[10px] uppercase font-bold text-slate-500">Oct</span>
                                            <span className="text-lg font-bold text-slate-900 dark:text-white leading-none">30</span>
                                        </div>
                                    </div>
                                    <p className="text-xs text-slate-500 pl-2">Verification required before submission.</p>
                                </div>

                                {/* Actions Area - Pushed to bottom of this column */}
                                <div className="flex flex-col gap-4 pt-4 border-t border-dashed border-gray-200 dark:border-[#3c4753] mt-2">
                                    <h2 className="text-slate-900 dark:text-white text-xl font-bold">Actions</h2>
                                    <div className="flex flex-col gap-3">
                                        <button
                                            onClick={() => navigate('/data-collection')}
                                            className="w-full bg-primary hover:bg-primary/90 text-white p-3 rounded-lg text-sm font-semibold transition-colors flex items-center justify-center gap-2 shadow-lg shadow-primary/20"
                                        >
                                            <PlusCircle size={20} />
                                            Start New Data Entry
                                        </button>
                                        <button className="w-full bg-white dark:bg-[#1e293b] border border-gray-200 dark:border-[#3c4753] hover:border-primary/50 text-slate-700 dark:text-white p-3 rounded-lg text-sm font-medium transition-colors flex items-center justify-center gap-2 shadow-sm hover:shadow-md">
                                            <HistoryIcon className="text-slate-500 dark:text-slate-400" size={20} />
                                            Review Previous Work
                                        </button>
                                        <button className="w-full bg-white dark:bg-[#1e293b] border border-gray-200 dark:border-[#3c4753] hover:border-primary/50 text-slate-700 dark:text-white p-3 rounded-lg text-sm font-medium transition-colors flex items-center justify-center gap-2 shadow-sm hover:shadow-md">
                                            <ClipboardCheck className="text-slate-500 dark:text-slate-400" size={20} />
                                            Perform QC
                                        </button>
                                    </div>
                                </div>

                            </div>
                        </section>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Dashboard;
