import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = (e) => {
        e.preventDefault();
        // Placeholder login logic
        navigate('/');
    };

    return (
        <div style={{
            minHeight: '100vh',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            position: 'relative',
            overflow: 'hidden'
        }}>
            {/* Background Orbs */}
            <div style={{
                position: 'absolute',
                top: '20%',
                left: '20%',
                width: '400px',
                height: '400px',
                background: 'radial-gradient(circle, var(--accent-primary) 0%, transparent 70%)',
                opacity: 0.2,
                filter: 'blur(60px)',
                zIndex: 0
            }}></div>
            <div style={{
                position: 'absolute',
                bottom: '20%',
                right: '20%',
                width: '300px',
                height: '300px',
                background: 'radial-gradient(circle, var(--accent-secondary) 0%, transparent 70%)',
                opacity: 0.2,
                filter: 'blur(60px)',
                zIndex: 0
            }}></div>

            <div className="glass-panel animate-fade-in" style={{
                width: '400px',
                padding: '40px',
                zIndex: 1,
                border: '1px solid rgba(255,255,255,0.1)'
            }}>
                <div style={{ textAlign: 'center', marginBottom: '32px' }}>
                    <h1 style={{ fontSize: '2rem', marginBottom: '8px' }}>CARRMOS</h1>
                    <p className="text-muted">Welcome back! Please sign in.</p>
                </div>

                <form onSubmit={handleLogin}>
                    <div style={{ marginBottom: '20px' }}>
                        <label style={{ display: 'block', marginBottom: '8px', fontSize: '0.9rem' }}>Email Address</label>
                        <input
                            type="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            style={{
                                width: '100%',
                                padding: '12px',
                                background: 'rgba(0,0,0,0.2)',
                                border: '1px solid var(--border-light)',
                                borderRadius: 'var(--radius-sm)',
                                color: 'white',
                                outline: 'none'
                            }}
                            placeholder="Enter your email"
                        />
                    </div>

                    <div style={{ marginBottom: '24px' }}>
                        <label style={{ display: 'block', marginBottom: '8px', fontSize: '0.9rem' }}>Password</label>
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            style={{
                                width: '100%',
                                padding: '12px',
                                background: 'rgba(0,0,0,0.2)',
                                border: '1px solid var(--border-light)',
                                borderRadius: 'var(--radius-sm)',
                                color: 'white',
                                outline: 'none'
                            }}
                            placeholder="••••••••"
                        />
                        <div style={{ textAlign: 'right', marginTop: '8px' }}>
                            <a href="#" style={{ fontSize: '0.8rem', color: 'var(--accent-primary)' }}>Forgot password?</a>
                        </div>
                    </div>

                    <button
                        type="submit"
                        style={{
                            width: '100%',
                            padding: '12px',
                            background: 'linear-gradient(135deg, var(--accent-primary), var(--accent-secondary))',
                            color: 'white',
                            border: 'none',
                            borderRadius: 'var(--radius-sm)',
                            fontSize: '1rem',
                            fontWeight: 600,
                            transition: 'transform 0.2s',
                        }}
                        onMouseOver={(e) => e.target.style.transform = 'scale(1.02)'}
                        onMouseOut={(e) => e.target.style.transform = 'scale(1)'}
                    >
                        Sign In
                    </button>
                </form>
            </div>
        </div>
    );
};

export default Login;
