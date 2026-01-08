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
    LogOut
} from 'lucide-react';

const Sidebar = () => {
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
            width: '260px',
            height: 'calc(100vh - 32px)',
            position: 'fixed',
            left: '16px',
            top: '16px',
            display: 'flex',
            flexDirection: 'column',
            padding: '24px 16px',
            zIndex: 10
        }}>
            <div className="flex-center" style={{ marginBottom: '32px', gap: '10px' }}>
                <div style={{
                    width: '32px',
                    height: '32px',
                    background: 'var(--accent-primary)',
                    borderRadius: '50%',
                }}></div>
                <h2 style={{ fontSize: '1.25rem', fontWeight: 700, letterSpacing: '-0.03em' }}>
                    CARRMOS
                </h2>
            </div>

            <nav style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: '4px', overflowY: 'auto' }}>
                {navItems.map((item) => (
                    <NavLink
                        key={item.path}
                        to={item.path}
                        className={({ isActive }) => `
              flex-center
              ${isActive ? 'active' : ''}
            `}
                        style={({ isActive }) => ({
                            justifyContent: 'flex-start',
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
                        <item.icon size={18} />
                        {item.label}
                    </NavLink>
                ))}
            </nav>

            <div style={{ marginTop: 'auto', paddingTop: '16px', borderTop: '1px solid var(--border-light)' }}>
                <button
                    className="flex-center"
                    style={{
                        width: '100%',
                        justifyContent: 'flex-start',
                        padding: '12px 16px',
                        background: 'transparent',
                        color: 'var(--text-muted)',
                        gap: '12px',
                        fontSize: '0.9rem'
                    }}
                >
                    <LogOut size={18} />
                    Sign Out
                </button>
            </div>
        </aside>
    );
};

export default Sidebar;
