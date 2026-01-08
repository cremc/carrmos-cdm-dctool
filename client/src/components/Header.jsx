import React from 'react';
import { useLocation } from 'react-router-dom';
import { Bell, Search } from 'lucide-react';

const Header = () => {
    const location = useLocation();

    const getPageTitle = (pathname) => {
        const format = (str) => str.replace('/', '').split('-').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join(' ');
        if (pathname === '/') return 'User Dashboard';
        if (pathname === '/review') return 'Data Review';
        if (pathname === '/collection') return 'Data Collection';
        if (pathname === '/quality') return 'Data Quality Check';
        if (pathname === '/edit-table') return 'Data Edit (Table)';
        if (pathname === '/edit-form') return 'Data Edit (Form)';
        if (pathname === '/relate') return 'Data Relate (DARMA)';
        if (pathname === '/manager') return 'Data Manager';
        if (pathname === '/migration') return 'Data Migration';
        if (pathname === '/analyzer') return 'Data Analyzer';
        if (pathname === '/users') return 'User Manager';
        if (pathname === '/access') return 'Access Manager';
        return format(pathname);
    };

    return (
        <header className="glass-panel" style={{
            height: '64px',
            margin: '0 0 24px 0',
            padding: '0 24px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            position: 'sticky',
            top: '16px',
            zIndex: 9
        }}>
            <div>
                <h1 style={{ fontSize: '1.25rem' }}>{getPageTitle(location.pathname)}</h1>
            </div>

            <div className="flex-center" style={{ gap: '20px' }}>
                <div className="flex-center" style={{
                    background: 'rgba(255,255,255,0.05)',
                    padding: '8px 12px',
                    borderRadius: '20px',
                    gap: '8px'
                }}>
                    <Search size={16} className="text-muted" />
                    <input
                        type="text"
                        placeholder="Search..."
                        style={{
                            background: 'transparent',
                            border: 'none',
                            outline: 'none',
                            color: 'var(--text-main)',
                            fontSize: '0.9rem',
                            width: '150px'
                        }}
                    />
                </div>

                <button className="flex-center" style={{
                    background: 'transparent',
                    color: 'var(--text-main)',
                    position: 'relative'
                }}>
                    <Bell size={20} />
                    <span style={{
                        position: 'absolute',
                        top: '-2px',
                        right: '-2px',
                        width: '8px',
                        height: '8px',
                        background: 'var(--accent-secondary)',
                        borderRadius: '50%'
                    }}></span>
                </button>

                <div className="flex-center" style={{ gap: '10px' }}>
                    <div style={{ textAlign: 'right' }}>
                        <p style={{ fontSize: '0.9rem', fontWeight: 500 }}>Atul User</p>
                        <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Admin</p>
                    </div>
                    <div style={{
                        width: '40px',
                        height: '40px',
                        background: 'linear-gradient(135deg, var(--accent-primary), var(--accent-secondary))',
                        borderRadius: '50%'
                    }}></div>
                </div>
            </div>
        </header>
    );
};

export default Header;
