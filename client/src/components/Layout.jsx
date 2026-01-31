import React from 'react';
import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar';
import Header from './Header';

const Layout = () => {
    const [isSidebarOpen, setIsSidebarOpen] = React.useState(true);
    const [isPinned, setIsPinned] = React.useState(true); // Default to pinned as per current behavior

    const toggleSidebar = () => setIsSidebarOpen(!isSidebarOpen);
    const togglePin = () => setIsPinned(!isPinned);

    // Calculate effective sidebar width for layout
    // If pinned and open, it takes space. Otherwise (collapsed or overlay), it takes fixed collapsed width space.
    const sidebarSpace = isSidebarOpen && isPinned ? '260px' : '64px';

    return (
        <div style={{ minHeight: '100vh', display: 'flex' }}>
            <Sidebar
                isOpen={isSidebarOpen}
                toggle={toggleSidebar}
                isPinned={isPinned}
                togglePin={togglePin}
            />
            <main style={{
                flex: 1,
                marginLeft: `calc(${sidebarSpace} + 32px)`, // width + 32px left gap to prevent overlap
                marginRight: '16px',
                paddingTop: '16px',
                paddingBottom: '16px',
                display: 'flex',
                flexDirection: 'column',
                transition: 'margin-left 0.3s ease'
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
