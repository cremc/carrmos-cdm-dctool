import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import DataReview from './pages/DataReview';
import DataCollection from './pages/DataCollection';
import DataQuality from './pages/DataQuality';
import DataEditBulk from './pages/DataEditBulk';
import DataEditIndividual from './pages/DataEditIndividual';
import DataRelate from './pages/DataRelate';
import DataManager from './pages/DataManager';
import DataMigration from './pages/DataMigration';
import DataAnalyzer from './pages/DataAnalyzer';
import UserManager from './pages/UserManager';
import AccessManager from './pages/AccessManager';
import Layout from './components/Layout';
import ProtectedRoute from './components/ProtectedRoute';
import './App.css';

function App() {
    // fast-track: temporary auth check until real auth is implemented
    const isAuthenticated = false;

    return (
        <Router>
            <Routes>
                <Route path="/login" element={<Login />} />

                <Route element={<ProtectedRoute />}>
                    <Route element={<Layout />}>
                        <Route path="/" element={<Navigate to="/dashboard" replace />} />
                        <Route path="/dashboard" element={<Dashboard />} />
                        <Route path="/data-review" element={<DataReview />} />
                        <Route path="/data-collection" element={<DataCollection />} />
                        <Route path="/data-quality" element={<DataQuality />} />
                        <Route path="/data-edit/bulk" element={<DataEditBulk />} />
                        <Route path="/data-edit/individual" element={<DataEditIndividual />} />
                        <Route path="/data-relate" element={<DataRelate />} />
                        <Route path="/data-manager" element={<DataManager />} />
                        <Route path="/data-migration" element={<DataMigration />} />
                        <Route path="/data-analyzer" element={<DataAnalyzer />} />
                        <Route path="/user-manager" element={<UserManager />} />
                        <Route path="/access-manager" element={<AccessManager />} />
                    </Route>
                </Route>
            </Routes>
        </Router>
    );
}

export default App;
