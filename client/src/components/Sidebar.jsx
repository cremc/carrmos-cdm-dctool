import React from 'react';
import { NavLink } from 'react-router-dom';
import {
    LayoutDashboard,
    FileSearch,
    PenTool,
    ClipboardCheck,
    Table2,
    FormInput,
    Network,
    Database,
    ArrowRightLeft,
    BarChart3,
    Users,
    ShieldCheck,
    LogOut,
    ChevronLeft,
    ChevronRight,
    Search,
    Pin,
    PinOff
} from 'lucide-react';

const Sidebar = ({ isOpen, toggle, isPinned, togglePin }) => {
    const navItems = [
        { path: '/dashboard', label: 'User Dashboard', icon: LayoutDashboard },
        { path: '/data-review', label: 'Data Review', icon: FileSearch },
        { path: '/data-collection', label: 'Data Collection', icon: PenTool },
        { path: '/data-quality', label: 'Data Quality Check', icon: ClipboardCheck },
        { path: '/data-edit/bulk', label: 'Data Edit (Bulk)', icon: Table2 },
        { path: '/data-edit/individual', label: 'Data Edit (Individual)', icon: FormInput },
        { path: '/data-relate', label: 'Data Relate (DARMA)', icon: Network },
        { path: '/data-manager', label: 'Data Manager', icon: Database },
        { path: '/data-migration', label: 'Data Migration', icon: ArrowRightLeft },
        { path: '/data-analyzer', label: 'Data Analyzer', icon: BarChart3 },
        { path: '/user-manager', label: 'User Manager', icon: Users },
        { path: '/access-manager', label: 'Access Manager', icon: ShieldCheck },
    ];

    return (
        <aside className="glass-panel" style={{
            width: isOpen ? '260px' : '64px',
            height: 'calc(100vh - 32px)',
            position: 'fixed',
            left: '16px',
            top: '16px',
            display: 'flex',
            flexDirection: 'column',
            padding: isOpen ? '24px 16px' : '24px 8px',
            zIndex: 50, // Higher z-index for overlay
            transition: 'width 0.3s ease, padding 0.3s ease, box-shadow 0.3s ease',
            overflow: 'hidden',
            // Add shadow when open but not pinned (overlay mode)
            boxShadow: isOpen && !isPinned ? '0 10px 40px -10px rgba(0,0,0,0.5)' : undefined,
            backgroundColor: isOpen && !isPinned ? '#161b22' : undefined // Ensure opacity in overlay
        }}>
            <div className={`flex items-center ${isOpen ? 'justify-start' : 'justify-center'}`} style={{ marginBottom: '32px', gap: '10px' }}>
                <div style={{
                    width: '32px',
                    height: '32px',
                    background: 'var(--accent-primary)',
                    borderRadius: '50%',
                    flexShrink: 0
                }}></div>
                {isOpen && (
                    <h2 style={{ fontSize: '1.25rem', fontWeight: 700, letterSpacing: '-0.03em', whiteSpace: 'nowrap' }}>
                        CARRMOS
                    </h2>
                )}
            </div>

            <nav style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: '4px', overflowY: 'auto', overflowX: 'hidden' }}>
                {navItems.map((item) => (
                    <NavLink
                        key={item.path}
                        to={item.path}
                        title={!isOpen ? item.label : ''}
                        className={({ isActive }) => `
              flex items-center
              ${isActive ? 'active' : ''}
            `}
                        style={({ isActive }) => ({
                            justifyContent: isOpen ? 'flex-start' : 'center',
                            padding: '12px 16px',
                            borderRadius: 'var(--radius-sm)',
                            color: isActive ? 'white' : 'var(--text-muted)',
                            background: isActive ? 'hsla(var(--hue-accent), 80%, 60%, 0.15)' : 'transparent',
                            transition: 'var(--transition-fast)',
                            gap: '12px',
                            fontSize: '0.9rem',
                            fontWeight: isActive ? 500 : 400
                        })}
                    >
                        <item.icon size={18} style={{ flexShrink: 0 }} />
                        {isOpen && <span style={{ whiteSpace: 'nowrap' }}>{item.label}</span>}
                    </NavLink>
                ))}
            </nav>

            {/* Toggle Button */}
            <button
                onClick={toggle}
                className="absolute top-[80px] -right-[10px] bg-slate-800 text-slate-400 border border-slate-600 rounded-full p-1 hover:text-white hover:border-slate-400 transition-colors z-20 shadow-md"
                style={{ width: '20px', height: '20px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}
                title={isOpen ? "Collapse" : "Expand"}
            >
                {isOpen ? <ChevronLeft size={12} /> : <ChevronRight size={12} />}
            </button>

            {/* Pin Button (Only visible when open) */}
            {isOpen && (
                <button
                    onClick={togglePin}
                    className="absolute top-[16px] right-[16px] text-slate-500 hover:text-white transition-colors"
                    title={isPinned ? "Unpin (Overlay Mode)" : "Pin Sidebar"}
                >
                    {isPinned ? <Pin size={16} fill="currentColor" /> : <PinOff size={16} />}
                </button>
            )}


            <div style={{ marginTop: 'auto', paddingTop: '16px', borderTop: '1px solid var(--border-light)' }}>
                <button
                    className={`flex items-center ${isOpen ? 'justify-start' : 'justify-center'}`}
                    style={{
                        width: '100%',
                        padding: '12px 16px',
                        background: 'transparent',
                        color: 'var(--text-muted)',
                        gap: '12px',
                        fontSize: '0.9rem'
                    }}
                >
                    <LogOut size={18} style={{ flexShrink: 0 }} />
                    {isOpen && <span style={{ whiteSpace: 'nowrap' }}>Sign Out</span>}
                </button>
            </div>
        </aside>
    );
};

export default Sidebar;
