import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { Mail, Lock, Eye, EyeOff, CheckCircle, ShieldCheck, LogIn, School } from 'lucide-react';

const Login = () => {
    const [showPassword, setShowPassword] = useState(false);
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [acceptedTerms, setAcceptedTerms] = useState(false);

    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setLoading(true);
        console.log('Login attempt:', { email });

        try {
            // Using URLSearchParams for x-www-form-urlencoded format required by OAuth2PasswordRequestForm
            const formData = new URLSearchParams();
            formData.append('username', email);
            formData.append('password', password);

            const response = await axios.post('/api/login/access-token', formData, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            });

            console.log('Login successful:', response.data);
            localStorage.setItem('token', response.data.access_token);
            navigate('/dashboard');
        } catch (err) {
            console.error('Login error:', err);
            if (err.response) {
                // Server responded with non-2xx status
                setError(err.response.data.detail || 'Login failed. Please check your credentials.');
            } else if (err.request) {
                // No response received
                setError('Unable to reach server. Please try again later.');
            } else {
                // Request setup error
                setError('An unexpected error occurred.');
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="bg-background-light dark:bg-background-dark text-slate-900 dark:text-white min-h-screen flex flex-col font-display antialiased selection:bg-primary/30 selection:text-primary">
            <header className="w-full flex items-center justify-between whitespace-nowrap border-b border-solid border-slate-200 dark:border-slate-800 px-6 py-4 bg-white dark:bg-background-dark sticky top-0 z-10">
                <div className="flex items-center gap-3">
                    <div className="size-8 flex items-center justify-center text-primary">
                        <School size={32} />
                    </div>
                    <h2 className="text-slate-900 dark:text-white text-lg font-bold leading-tight tracking-tight">Carrmos Data Collector</h2>
                </div>
                <div>
                    <a className="text-sm font-medium text-slate-500 hover:text-primary dark:text-slate-400 dark:hover:text-primary transition-colors" href="#">Help & Support</a>
                </div>
            </header>

            <main className="flex-grow flex items-center justify-center p-4 sm:p-8">
                <div className="w-full max-w-6xl grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                    {/* Left Side - Visual/Info */}
                    <div className="hidden lg:flex flex-col gap-6 pr-8">
                        <div className="relative w-full h-80 rounded-xl overflow-hidden shadow-2xl bg-slate-800 flex items-center justify-center p-8">
                            <div className="absolute inset-0 bg-gradient-to-br from-primary/10 via-background-dark to-slate-900"></div>
                            {/* Simplified Visual Representation of the Flow Diagram using CSS/Divs */}
                            <div className="relative w-full h-full flex flex-col items-center justify-center gap-6 z-10">
                                <div className="flex justify-between w-full gap-2 max-w-sm">
                                    {[...Array(5)].map((_, i) => (
                                        <div key={i} className="w-12 h-16 bg-slate-700/80 rounded border border-slate-600 flex flex-col gap-1 p-1">
                                            <div className="h-1 w-full bg-slate-500 rounded-sm mb-1"></div>
                                            <div className="h-1 w-2/3 bg-slate-500 rounded-sm"></div>
                                        </div>
                                    ))}
                                </div>
                                <div className="flex justify-center w-full h-8 relative max-w-sm">
                                    {/* Arrows (simplified) */}
                                    <div className="text-primary/60 font-bold rotate-180">↓↓↓</div>
                                </div>
                                <div className="w-24 h-20 bg-slate-800 rounded-md border-2 border-primary/50 flex flex-col gap-2 p-2 shadow-lg shadow-primary/10 relative z-10">
                                    <div className="flex gap-1 items-end h-8 border-b border-slate-700 pb-1">
                                        <div className="w-2 bg-primary/40 h-3 rounded-t-sm"></div>
                                        <div className="w-2 bg-primary/60 h-5 rounded-t-sm"></div>
                                        <div className="w-2 bg-primary/80 h-4 rounded-t-sm"></div>
                                        <div className="w-2 bg-primary h-6 rounded-t-sm"></div>
                                    </div>
                                    <div className="grid grid-cols-3 gap-1">
                                        {[...Array(6)].map((_, i) => <div key={i} className="h-1 bg-slate-600 rounded-sm"></div>)}
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div>
                            <h1 className="text-3xl font-black tracking-tight text-slate-900 dark:text-white mb-2">
                                CDM Data Collection
                            </h1>
                            <p className="text-lg text-slate-600 dark:text-slate-400 leading-relaxed">
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim.
                            </p>
                        </div>
                        <div className="flex items-center gap-4 mt-4 text-sm text-slate-500 dark:text-slate-500">
                            <div className="flex items-center gap-1">
                                <Lock size={18} />
                                <span>End-to-end Encrypted</span>
                            </div>
                            <div className="flex items-center gap-1">
                                <ShieldCheck size={18} />
                                <span>Authorized Personnel Only</span>
                            </div>
                        </div>
                    </div>

                    {/* Right Side - Login Form */}
                    <div className="w-full max-w-md mx-auto">
                        <div className="bg-white dark:bg-card-dark rounded-xl shadow-xl dark:shadow-black/40 border border-slate-200 dark:border-slate-800 p-8 sm:p-10 flex flex-col gap-6">
                            <div className="flex flex-col gap-2 mb-2">
                                <h2 className="text-2xl font-bold text-slate-900 dark:text-white">Sign In</h2>
                                <p className="text-slate-500 dark:text-slate-400">Please enter the credentials given to you.</p>
                            </div>
                            <form className="flex flex-col gap-5" onSubmit={handleSubmit}>
                                {error && (
                                    <div className="bg-red-50 text-red-600 p-3 rounded-lg text-sm border border-red-200">
                                        {error}
                                    </div>
                                )}
                                <div className="flex flex-col gap-1.5">
                                    <label className="text-sm font-medium text-slate-700 dark:text-slate-200" htmlFor="email">Email</label>
                                    <div className="relative group">
                                        <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400 group-focus-within:text-primary transition-colors">
                                            <Mail size={20} />
                                        </div>
                                        <input
                                            className="w-full h-12 rounded-lg border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-background-dark px-10 text-base text-slate-900 dark:text-white placeholder:text-slate-400 focus:border-primary focus:ring-1 focus:ring-primary focus:outline-none transition-all"
                                            id="email"
                                            placeholder="name@companyname.com"
                                            type="email"
                                            value={email}
                                            onChange={(e) => setEmail(e.target.value)}
                                        />
                                    </div>
                                </div>
                                <div className="flex flex-col gap-1.5">
                                    <div className="flex items-center justify-between">
                                        <label className="text-sm font-medium text-slate-700 dark:text-slate-200" htmlFor="password">Password</label>
                                        <a className="text-sm font-medium text-primary hover:text-blue-400 transition-colors" href="#">Forgot password?</a>
                                    </div>
                                    <div className="relative group">
                                        <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400 group-focus-within:text-primary transition-colors">
                                            <Lock size={20} />
                                        </div>
                                        <input
                                            className="w-full h-12 rounded-lg border border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-background-dark pl-10 pr-10 text-base text-slate-900 dark:text-white placeholder:text-slate-400 focus:border-primary focus:ring-1 focus:ring-primary focus:outline-none transition-all"
                                            id="password"
                                            placeholder="Enter your password"
                                            type={showPassword ? "text" : "password"}
                                            value={password}
                                            onChange={(e) => setPassword(e.target.value)}
                                        />
                                        <button
                                            className="absolute inset-y-0 right-0 pr-3 flex items-center text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 cursor-pointer transition-colors"
                                            type="button"
                                            onClick={() => setShowPassword(!showPassword)}
                                        >
                                            {showPassword ? <EyeOff size={20} /> : <Eye size={20} />}
                                        </button>
                                    </div>
                                </div>
                                <div className="flex items-start gap-3 py-1">
                                    <div className="relative flex items-center h-5">
                                        <input
                                            className="h-4 w-4 rounded border-slate-300 dark:border-slate-600 text-primary bg-slate-50 dark:bg-background-dark focus:ring-offset-0 focus:ring-primary cursor-pointer"
                                            id="terms"
                                            type="checkbox"
                                            checked={acceptedTerms}
                                            onChange={(e) => setAcceptedTerms(e.target.checked)}
                                        />
                                    </div>
                                    <label className="text-sm text-slate-600 dark:text-slate-400 leading-tight" htmlFor="terms">
                                        I agree to the <a className="text-primary hover:underline" href="#">Terms of Service</a> and <a className="text-primary hover:underline" href="#">Privacy Policy</a>.
                                    </label>
                                </div>
                                <button className="w-full h-12 mt-2 bg-primary hover:bg-blue-600 text-white font-bold rounded-lg shadow-lg shadow-primary/20 hover:shadow-primary/40 transition-all transform active:scale-[0.98] flex items-center justify-center gap-2">
                                    <span>Sign In</span>
                                    <LogIn size={20} />
                                </button>
                            </form>
                            <div className="mt-2 text-center border-t border-slate-200 dark:border-slate-700 pt-6">
                                <p className="text-sm text-slate-500 dark:text-slate-400">
                                    Having trouble accessing your account? <br className="sm:hidden" />
                                    <a className="font-medium text-slate-700 dark:text-slate-200 hover:text-primary transition-colors" href="#">Contact IT Administration</a>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
            <footer className="py-6 text-center text-xs text-slate-400 dark:text-slate-600">
                © 2025-26 Carrmos Solutions. All rights reserved.
            </footer>
        </div>
    );
};

export default Login;
