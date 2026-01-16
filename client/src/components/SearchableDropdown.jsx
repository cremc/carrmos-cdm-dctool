import React, { useState, useRef, useEffect } from 'react';
import { ChevronDown, Search, X } from 'lucide-react';

const SearchableDropdown = ({ options = [], value, onChange, placeholder = "Select...", label, disabled = false }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [searchTerm, setSearchTerm] = useState('');
    const wrapperRef = useRef(null);
    const inputRef = useRef(null);

    // Filter options based on search term
    const filteredOptions = options.filter(option =>
        option.label.toLowerCase().includes(searchTerm.toLowerCase())
    );

    // Close dropdown when clicking outside
    useEffect(() => {
        const handleClickOutside = (event) => {
            if (wrapperRef.current && !wrapperRef.current.contains(event.target)) {
                setIsOpen(false);
            }
        };
        document.addEventListener('mousedown', handleClickOutside);
        return () => document.removeEventListener('mousedown', handleClickOutside);
    }, []);

    const handleSelect = (option) => {
        onChange(option);
        setIsOpen(false);
        setSearchTerm(''); // Optional: clear search on select
    };

    const handleInputFocus = () => {
        if (!disabled) setIsOpen(true);
    };

    return (
        <div className="flex flex-col gap-1.5 w-full relative" ref={wrapperRef}>
            {label && <label className="text-xs font-semibold text-slate-500 uppercase tracking-wider">{label}</label>}

            <div
                className={`
                    flex items-center justify-between w-full p-3 rounded-lg border bg-white dark:bg-[#1e293b] 
                    cursor-pointer transition-all duration-200
                    ${isOpen ? 'border-primary ring-2 ring-primary/20' : 'border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600'}
                    ${disabled ? 'opacity-50 cursor-not-allowed bg-slate-100 dark:bg-slate-800' : ''}
                `}
                onClick={() => !disabled && setIsOpen(!isOpen)}
            >
                <div className="flex-1 truncate text-sm font-medium text-slate-900 dark:text-white">
                    {value ? value.label : <span className="text-slate-400">{placeholder}</span>}
                </div>
                <ChevronDown size={18} className={`text-slate-400 transition-transform ${isOpen ? 'rotate-180' : ''}`} />
            </div>

            {isOpen && !disabled && (
                <div className="absolute top-full left-0 right-0 mt-2 bg-white dark:bg-[#1e293b] border border-slate-200 dark:border-slate-700 rounded-lg shadow-xl z-50 overflow-hidden flex flex-col max-h-60 animate-in fade-in zoom-in-95 duration-100 origin-top">
                    {/* Search Input */}
                    <div className="p-2 border-b border-slate-100 dark:border-slate-800 sticky top-0 bg-white dark:bg-[#1e293b]">
                        <div className="relative">
                            <Search size={14} className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
                            <input
                                ref={inputRef}
                                type="text"
                                className="w-full text-sm pl-9 pr-3 py-2 bg-slate-50 dark:bg-[#111418] border border-slate-200 dark:border-slate-700 rounded-md focus:outline-none focus:ring-1 focus:ring-primary focus:border-primary text-slate-900 dark:text-white placeholder:text-slate-400"
                                placeholder="Search..."
                                value={searchTerm}
                                onChange={(e) => setSearchTerm(e.target.value)}
                                onClick={(e) => e.stopPropagation()}
                                autoFocus
                            />
                        </div>
                    </div>

                    {/* Options List */}
                    <div className="overflow-y-auto overflow-x-hidden flex-1 p-1">
                        {filteredOptions.length > 0 ? (
                            filteredOptions.map((option) => (
                                <div
                                    key={option.value}
                                    className={`
                                        px-3 py-2 rounded-md text-sm cursor-pointer flex items-center justify-between
                                        ${value?.value === option.value
                                            ? 'bg-primary/10 text-primary font-semibold'
                                            : 'text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-[#252f3e]'}
                                    `}
                                    onClick={(e) => {
                                        e.stopPropagation();
                                        handleSelect(option);
                                    }}
                                >
                                    {option.label}
                                    {value?.value === option.value && <X size={14} className="opacity-0" />} {/* Spacer / Check */}
                                </div>
                            ))
                        ) : (
                            <div className="p-4 text-center text-xs text-slate-400">
                                No results found.
                            </div>
                        )}
                    </div>
                </div>
            )}
        </div>
    );
};

export default SearchableDropdown;
