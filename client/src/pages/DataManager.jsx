import React, { useState } from 'react';
import { Search, UserPlus, Filter, MoreVertical, Edit2, Trash2, Shield, User, MapPin, Activity, Save, X } from 'lucide-react';
import SearchableDropdown from '../components/SearchableDropdown';
import { createUser } from '../utils/api';

const DataManager = () => {
    const [activeTab, setActiveTab] = useState('create-user');
    const [searchQuery, setSearchQuery] = useState('');

    // Mock Data for User List
    const users = [
        { id: 1, name: 'Aditi Sharma', email: 'a.sharma@cpdsolutions.in', role: 'QC Checker', scope: 'West Zone', scopeDetail: 'Maharashtra, Gujarat', status: 'Active', avatar: 'AS' },
        { id: 2, name: 'Rajesh Kumar', email: 'r.kumar@cpdsolutions.in', role: 'Data Collector', scope: 'North Zone', scopeDetail: 'Delhi NCR', status: 'Active', avatar: 'RK' },
        { id: 3, name: 'Vikram Sethi', email: 'v.sethi@cpdsolutions.in', role: 'Data Manager', scope: 'All Zones', scopeDetail: 'Pan India', status: 'Active', avatar: 'VS' },
        { id: 4, name: 'Priya Singh', email: 'p.singh@cpdsolutions.in', role: 'Data Collector', scope: 'South Zone', scopeDetail: 'Karnataka, Tamil Nadu', status: 'Inactive', avatar: 'PS' },
    ];

    // Form State
    const [formData, setFormData] = useState({
        email: '',
        password: 'CPD_78XyZ_2024',
        role: null,
        firstName: '',
        lastName: '',
        region: null,
        status: null
    });

    const roles = [
        { label: 'Data Manager', value: 'manager' },
        { label: 'QC Checker', value: 'qc' },
        { label: 'Data Collector', value: 'collector' },
        { label: 'Admin', value: 'admin' }
    ];

    const regions = [
        { label: 'All India', value: 'all' },
        { label: 'North Zone (Delhi NCR)', value: 'north' },
        { label: 'South Zone (Bangalore/Chennai)', value: 'south' },
        { label: 'West Zone (Mumbai/Pune)', value: 'west' },
        { label: 'East Zone (Kolkata)', value: 'east' }
    ];

    const statusOptions = [
        { label: 'Active', value: 'active' },
        { label: 'Inactive', value: 'inactive' },
        { label: 'Suspended', value: 'suspended' }
    ];

    const isFormValid = formData.email && formData.password && formData.role && formData.firstName && formData.lastName && formData.region && formData.status;

    const handleAddUser = async () => {
        if (!isFormValid) return;

        try {
            const userData = {
                email: formData.email,
                password: formData.password,
                db_role: { 'manager': 2, 'qc': 3, 'collector': 4, 'admin': 5 }[formData.role.value] || 1, // Mapping role to ID
                first_name: formData.firstName,
                last_name: formData.lastName,
                is_active: formData.status.value === 'active'
            };

            await createUser(userData);
            alert('User created successfully!');
            // Reset form
            setFormData({
                email: '',
                password: 'CPD_' + Math.random().toString(36).slice(-8), // Simple random password regen
                role: null,
                firstName: '',
                lastName: '',
                region: null,
                status: null
            });
        } catch (error) {
            alert('Failed to create user. See console for details.');
            console.error(error);
        }
    };

    return (
        <div className="flex h-full gap-6 overflow-hidden">
            {/* LEFT PANEL - User List (65%) */}
            <div className="flex-[65] flex flex-col gap-4 min-w-0">
                {/* Header & Controls */}
                <div className="flex flex-col gap-1">
                    <div className="flex items-center text-sm text-slate-400 gap-2 mb-1">
                        <span>Home</span> / <span>Data Management</span> / <span className="text-slate-200">User Administration</span>
                    </div>
                    <h1 className="text-3xl font-bold text-white tracking-tight">Data Manager</h1>
                    <p className="text-slate-400 text-sm">Career Planning and Development solutions data collection management interface.</p>
                </div>

                <div className="glass-panel p-4 flex flex-col gap-4 flex-1 min-h-0">
                    {/* Search & Filter Bar */}
                    <div className="flex items-center gap-3">
                        <div className="relative flex-1">
                            <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" size={18} />
                            <input
                                type="text"
                                placeholder="Search data points..."
                                className="w-full bg-slate-900/50 border border-slate-700 text-white text-sm rounded-lg pl-10 pr-4 py-2.5 focus:outline-none focus:border-blue-500 transition-colors"
                                value={searchQuery}
                                onChange={(e) => setSearchQuery(e.target.value)}
                            />
                        </div>
                        <div className="w-40">
                            <SearchableDropdown
                                placeholder="All Roles"
                                options={roles}
                                value={null} // TODO: Add filter state
                                onChange={() => { }}
                            />
                        </div>
                        <div className="w-40">
                            <SearchableDropdown
                                placeholder="All Statuses"
                                options={statusOptions}
                                value={null} // TODO: Add filter state
                                onChange={() => { }}
                            />
                        </div>
                    </div>

                    {/* Table Header */}
                    <div className="grid grid-cols-12 gap-4 px-4 py-2 text-xs font-bold text-slate-400 uppercase tracking-wider border-b border-slate-700/50">
                        <div className="col-span-4">User</div>
                        <div className="col-span-2">Role</div>
                        <div className="col-span-3">Access Scope</div>
                        <div className="col-span-2">Status</div>
                        <div className="col-span-1 text-center">Actions</div>
                    </div>

                    {/* User List */}
                    <div className="flex-1 overflow-y-auto -mx-2 px-2 space-y-2">
                        {users.map((user) => (
                            <div key={user.id} className="grid grid-cols-12 gap-4 items-center p-3 rounded-lg hover:bg-white/5 transition-colors border border-transparent hover:border-white/5 group">
                                {/* User Info */}
                                <div className="col-span-4 flex items-center gap-3 min-w-0">
                                    <div className={`w-10 h-10 rounded-full flex items-center justify-center text-sm font-bold shadow-lg
                                        ${user.role === 'Data Manager' ? 'bg-gradient-to-br from-blue-500 to-indigo-600 text-white' : ''}
                                        ${user.role === 'QC Checker' ? 'bg-gradient-to-br from-emerald-500 to-teal-600 text-white' : ''}
                                        ${user.role === 'Data Collector' ? 'bg-slate-700 text-slate-300' : ''}
                                    `}>
                                        {user.avatar}
                                    </div>
                                    <div className="flex flex-col min-w-0">
                                        <span className="text-sm font-semibold text-slate-200 truncate">{user.name}</span>
                                        <span className="text-xs text-slate-500 truncate">{user.email}</span>
                                    </div>
                                </div>

                                {/* Role */}
                                <div className="col-span-2">
                                    <span className={`inline-flex items-center px-2.5 py-1 rounded-full text-xs font-medium border
                                        ${user.role === 'Data Manager' ? 'bg-blue-500/10 text-blue-400 border-blue-500/20' : ''}
                                        ${user.role === 'QC Checker' ? 'bg-purple-500/10 text-purple-400 border-purple-500/20' : ''}
                                        ${user.role === 'Data Collector' ? 'bg-slate-700/30 text-slate-400 border-slate-600/30' : ''}
                                    `}>
                                        {user.role}
                                    </span>
                                </div>

                                {/* Access Scope */}
                                <div className="col-span-3 flex flex-col min-w-0 justify-center">
                                    <span className="text-sm text-slate-300 truncate">{user.scope}</span>
                                    <span className="text-xs text-slate-500 truncate">{user.scopeDetail}</span>
                                </div>

                                {/* Status */}
                                <div className="col-span-2">
                                    <div className="flex items-center gap-2">
                                        <div className={`w-2 h-2 rounded-full ${user.status === 'Active' ? 'bg-emerald-500 shadow-[0_0_8px_rgba(16,185,129,0.4)]' : 'bg-slate-600'}`}></div>
                                        <span className={`text-sm ${user.status === 'Active' ? 'text-emerald-500' : 'text-slate-500'}`}>{user.status}</span>
                                    </div>
                                </div>

                                {/* Actions */}
                                <div className="col-span-1 flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                                    <button className="p-1.5 text-slate-400 hover:text-white hover:bg-slate-700 rounded-md transition-colors">
                                        <Edit2 size={14} />
                                    </button>
                                    <button className="p-1.5 text-slate-400 hover:text-red-400 hover:bg-red-500/10 rounded-md transition-colors">
                                        <Trash2 size={14} />
                                    </button>
                                </div>
                            </div>
                        ))}
                    </div>

                    {/* Pagination / Footer */}
                    <div className="flex items-center justify-between text-xs text-slate-500 pt-3 border-t border-slate-700/30">
                        <span>Showing 1 to 4 of 24 entries</span>
                        <div className="flex gap-1">
                            <button className="px-2 py-1 rounded hover:bg-slate-800 disabled:opacity-50">Previous</button>
                            <button className="px-2 py-1 rounded bg-blue-600 text-white">1</button>
                            <button className="px-2 py-1 rounded hover:bg-slate-800">2</button>
                            <button className="px-2 py-1 rounded hover:bg-slate-800">Next</button>
                        </div>
                    </div>
                </div>
            </div>

            {/* RIGHT PANEL - Assignment Panel (35%) */}
            <div className="flex-[35] flex flex-col gap-4 min-w-[350px]">
                {/* Add New User Button */}
                <div className="flex justify-end pt-8">
                    <button className="flex items-center gap-2 bg-blue-600 hover:bg-blue-500 text-white px-4 py-2.5 rounded-lg text-sm font-medium transition-all shadow-lg shadow-blue-900/20 active:scale-95">
                        <UserPlus size={18} />
                        Add New User
                    </button>
                </div>

                {/* Tabs & Content */}
                <div className="glass-panel flex flex-col flex-1 overflow-hidden">
                    {/* Tabs Header */}
                    <div className="flex border-b border-slate-700/50">
                        <button
                            onClick={() => setActiveTab('create-user')}
                            className={`flex-1 py-4 text-sm font-medium border-b-2 transition-colors
                                ${activeTab === 'create-user' ? 'border-blue-500 text-blue-400' : 'border-transparent text-slate-400 hover:text-slate-200'}
                            `}
                        >
                            Create User
                        </button>
                        <button
                            onClick={() => setActiveTab('manage-access')}
                            className={`flex-1 py-4 text-sm font-medium border-b-2 transition-colors
                                ${activeTab === 'manage-access' ? 'border-blue-500 text-blue-400' : 'border-transparent text-slate-400 hover:text-slate-200'}
                            `}
                        >
                            Manage Access
                        </button>
                        <button
                            onClick={() => setActiveTab('manage-tasks')}
                            className={`flex-1 py-4 text-sm font-medium border-b-2 transition-colors
                                ${activeTab === 'manage-tasks' ? 'border-blue-500 text-blue-400' : 'border-transparent text-slate-400 hover:text-slate-200'}
                            `}
                        >
                            Manage Tasks
                        </button>
                    </div>

                    {/* Tab Content */}
                    <div className="flex-1 overflow-y-auto p-6 scrollbar-thin">
                        {activeTab === 'create-user' && (
                            <div className="flex flex-col gap-5 animate-in fade-in slide-in-from-right-4 duration-300">

                                {/* User Email */}
                                <div className="space-y-1.5">
                                    <label className="text-xs font-semibold text-slate-500 uppercase tracking-wider">User Email</label>
                                    <input
                                        type="email"
                                        placeholder="e.g. user@cpdsolutions.in"
                                        className="w-full bg-slate-900/30 border border-slate-700 rounded-lg px-3 py-2.5 text-sm text-white focus:outline-none focus:border-blue-500 transition-colors"
                                        value={formData.email}
                                        onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                                    />
                                </div>

                                {/* Generated Password */}
                                <div className="space-y-1.5">
                                    <label className="text-xs font-semibold text-slate-500 uppercase tracking-wider">Generated Password</label>
                                    <div className="relative group">
                                        <input
                                            type="text"
                                            readOnly
                                            value={formData.password}
                                            className="w-full bg-slate-900/50 border border-slate-700 rounded-lg px-3 py-2.5 text-sm text-slate-300 font-mono focus:outline-none cursor-copy"
                                        />
                                        <div className="text-[10px] text-slate-500 mt-1 italic">
                                            Auto-generated for security. Share with user via secure channel.
                                        </div>
                                    </div>
                                </div>

                                {/* DB Role */}
                                <SearchableDropdown
                                    label="DB Role"
                                    placeholder="Select Role"
                                    options={roles}
                                    value={formData.role}
                                    onChange={(val) => setFormData({ ...formData, role: val })}
                                />

                                {/* First & Last Name */}
                                <div className="grid grid-cols-2 gap-4">
                                    <div className="space-y-1.5">
                                        <label className="text-xs font-semibold text-slate-500 uppercase tracking-wider">First Name</label>
                                        <input
                                            type="text"
                                            placeholder="John"
                                            className="w-full bg-slate-900/30 border border-slate-700 rounded-lg px-3 py-2.5 text-sm text-white focus:outline-none focus:border-blue-500 transition-colors"
                                            value={formData.firstName}
                                            onChange={(e) => setFormData({ ...formData, firstName: e.target.value })}
                                        />
                                    </div>
                                    <div className="space-y-1.5">
                                        <label className="text-xs font-semibold text-slate-500 uppercase tracking-wider">Last Name</label>
                                        <input
                                            type="text"
                                            placeholder="Doe"
                                            className="w-full bg-slate-900/30 border border-slate-700 rounded-lg px-3 py-2.5 text-sm text-white focus:outline-none focus:border-blue-500 transition-colors"
                                            value={formData.lastName}
                                            onChange={(e) => setFormData({ ...formData, lastName: e.target.value })}
                                        />
                                    </div>
                                </div>

                                {/* Access Region */}
                                <SearchableDropdown
                                    label="Access Region"
                                    placeholder="Select Region"
                                    options={regions}
                                    value={formData.region}
                                    onChange={(val) => setFormData({ ...formData, region: val })}
                                />

                                {/* Status */}
                                <SearchableDropdown
                                    label="Status"
                                    placeholder="Select Status"
                                    options={statusOptions}
                                    value={formData.status}
                                    onChange={(val) => setFormData({ ...formData, status: val })}
                                />
                            </div>
                        )}

                        {activeTab === 'manage-access' && (
                            <div className="flex flex-col items-center justify-center h-full text-slate-500">
                                <Shield size={48} className="mb-4 opacity-20" />
                                <p>Manage Access (Content Pending)</p>
                            </div>
                        )}

                        {activeTab === 'manage-tasks' && (
                            <div className="flex flex-col items-center justify-center h-full text-slate-500">
                                <Activity size={48} className="mb-4 opacity-20" />
                                <p>Manage Tasks (Content Pending)</p>
                            </div>
                        )}
                    </div>

                    {/* Footer Actions (Only for Create User Tab) */}
                    {activeTab === 'create-user' && (
                        <div className="p-4 border-t border-slate-700/50 flex justify-end gap-3 bg-slate-900/20">
                            <button className="px-4 py-2 text-sm text-slate-400 hover:text-white transition-colors">
                                Clear Form
                            </button>
                            <button
                                onClick={handleAddUser}
                                disabled={!isFormValid}
                                className={`px-6 py-2 rounded-lg text-sm font-medium transition-all shadow-lg shadow-blue-900/20 active:scale-95
                                    ${isFormValid
                                        ? 'bg-blue-600 hover:bg-blue-500 text-white cursor-pointer'
                                        : 'bg-slate-700 text-slate-400 cursor-not-allowed opacity-50'
                                    }
                                `}
                            >
                                Create this user
                            </button>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default DataManager;
