import React from 'react';
import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar';
import Header from './Header';

const Layout = () => {
    return (
        <div style={{ minHeight: '100vh', display: 'flex' }}>
            <Sidebar />
            <main style={{
                flex: 1,
                marginLeft: '292px', // 260px width + 16px left + 16px gap
                marginRight: '16px',
                paddingTop: '16px',
                paddingBottom: '16px',
                display: 'flex',
                flexDirection: 'column'
            }}>
                <Header />
                <div className="glass-panel" style={{
                    flex: 1,
                    padding: '24px'
                }}>
                    <Outlet />
                </div>
            </main>
        </div>
    );
};

export default Layout;
