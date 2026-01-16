import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';

const ProtectedRoute = () => {
    // In a real app, you might validate the token expiration here
    // or use a global AuthContext.
    const token = localStorage.getItem('token');

    if (!token) {
        // Redirect to login if no token is found
        return <Navigate to="/login" replace />;
    }

    // If authenticated, render the child routes (Outlet)
    return <Outlet />;
};

export default ProtectedRoute;
