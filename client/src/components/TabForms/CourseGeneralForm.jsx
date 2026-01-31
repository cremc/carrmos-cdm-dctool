import React, { useState, useEffect } from 'react';
import { ChevronDown, Check } from 'lucide-react';
import SearchableDropdown from '../SearchableDropdown';

// Mock Data for Dropdowns
const ACADEMIC_LEVELS = [
    { value: 'undergraduate', label: 'Undergraduate' },
    { value: 'postgraduate', label: 'Postgraduate' },
    { value: 'diploma', label: 'Diploma' },
    { value: 'phd', label: 'PhD' }
];

const DISCIPLINE_GROUPS = [
    { value: 'engineering', label: 'Engineering & Technology' },
    { value: 'medical', label: 'Medical & Health Sciences' },
    { value: 'arts', label: 'Arts & Humanities' },
    { value: 'business', label: 'Business & Management' }
];

const DISCIPLINES = [
    { value: 'cs', label: 'Computer Science' },
    { value: 'mechanical', label: 'Mechanical Engineering' },
    { value: 'civil', label: 'Civil Engineering' },
    { value: 'electronics', label: 'Electronics & Communication' }
];

const COUNTRIES = [
    { value: 'india', label: 'India' },
    { value: 'usa', label: 'USA' },
    { value: 'uk', label: 'UK' },
    { value: 'canada', label: 'Canada' }
];

const STATES = [
    { value: 'karnataka', label: 'Karnataka' },
    { value: 'maharashtra', label: 'Maharashtra' },
    { value: 'delhi', label: 'Delhi' },
    { value: 'tamil_nadu', label: 'Tamil Nadu' }
];

const CURRENCIES = [
    { value: 'INR', label: 'INR' },
    { value: 'USD', label: 'USD' },
    { value: 'GBP', label: 'GBP' },
    { value: 'EUR', label: 'EUR' }
];

const CHECKBOX_OPTIONS = [
    { id: 'name', label: 'Name' },
    { id: 'description', label: 'Description' },
    { id: 'duration', label: 'Course duration' },
    { id: 'rigour', label: 'Rigour and challenges' },
    { id: 'tuition', label: 'Course tuition cost range' },
    { id: 'career', label: 'Career prospects after completion' },
    { id: 'group1', label: 'Course Base group' },
    { id: 'group2', label: 'Course domain' }
];

const CourseGeneralForm = ({ formData, onChange }) => {

    // Ensure nested state exists
    const {
        academicLevel, disciplineGroup, discipline, country, state, selectedCheckboxes,
        descLength, currency, otherSpecs
    } = formData || {};

    const handleDropdownChange = (field, option) => {
        onChange({
            ...formData,
            [field]: option
        });
    };

    const handleCheckboxChange = (id) => {
        onChange({
            ...formData,
            selectedCheckboxes: {
                ...selectedCheckboxes,
                [id]: !selectedCheckboxes?.[id]
            }
        });
    };

    const handleSpecChange = (field, value) => {
        onChange({
            ...formData,
            [field]: value
        });
    };

    return (
        <div className="grid grid-cols-12 gap-6 h-full p-1">
            {/* Column 1: Dropdowns (40% - spanned as 5/12) */}
            <div className="col-span-5 flex flex-col gap-4 overflow-y-auto pr-2">
                <SearchableDropdown
                    label="Academic Level"
                    options={ACADEMIC_LEVELS}
                    placeholder="Academic Level..."
                    value={academicLevel}
                    onChange={(opt) => handleDropdownChange('academicLevel', opt)}
                />

                <div className="flex gap-2">
                    <div className="flex-1">
                        <SearchableDropdown
                            label="Discipline Group"
                            options={DISCIPLINE_GROUPS}
                            placeholder="Discipline Group..."
                            value={disciplineGroup}
                            onChange={(opt) => handleDropdownChange('disciplineGroup', opt)}
                        />
                    </div>
                </div>

                <SearchableDropdown
                    label="Discipline"
                    options={DISCIPLINES}
                    placeholder="Discipline..."
                    value={discipline}
                    onChange={(opt) => handleDropdownChange('discipline', opt)}
                />

                <div className="grid grid-cols-2 gap-2">
                    <SearchableDropdown
                        label="Country"
                        options={COUNTRIES}
                        placeholder="Country..."
                        value={country}
                        onChange={(opt) => handleDropdownChange('country', opt)}
                    />
                    <SearchableDropdown
                        label="State/Prov"
                        options={STATES}
                        placeholder="State/Prov..."
                        value={state}
                        onChange={(opt) => handleDropdownChange('state', opt)}
                    />
                </div>
            </div>

            {/* Column 2: Checkboxes (30% - spanned as 4/12) */}
            <div className="col-span-4 flex flex-col gap-4 border-l border-r border-slate-800/50 px-4">
                <div className="flex flex-col gap-3 mt-2">
                    <div className="grid grid-cols-2 gap-x-2 gap-y-3">
                        {CHECKBOX_OPTIONS.map(opt => (
                            <label key={opt.id} className="flex items-start gap-2 cursor-pointer group">
                                <div className={`
                                    w-4 h-4 rounded border flex items-center justify-center mt-0.5 transition-colors
                                    ${selectedCheckboxes?.[opt.id]
                                        ? 'bg-primary border-primary text-white'
                                        : 'border-slate-600 bg-slate-800 group-hover:border-slate-500'}
                                `}>
                                    {selectedCheckboxes?.[opt.id] && <Check size={10} strokeWidth={4} />}
                                    <input
                                        type="checkbox"
                                        className="hidden"
                                        checked={!!selectedCheckboxes?.[opt.id]}
                                        onChange={() => handleCheckboxChange(opt.id)}
                                    />
                                </div>
                                <span className={`text-sm leading-tight ${selectedCheckboxes?.[opt.id] ? 'text-slate-200' : 'text-slate-500'}`}>
                                    {opt.label}
                                </span>
                            </label>
                        ))}
                    </div>
                </div>
            </div>

            {/* Column 3: Specs (30% - spanned as 3/12) */}
            <div className="col-span-3 flex flex-col gap-4 pl-2">
                <div className="grid grid-cols-2 gap-2">
                    <div className="flex flex-col gap-1.5">
                        <label className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Currency</label>
                        <div className="relative">
                            <select
                                className="w-full bg-slate-900 border border-slate-700 rounded p-2 text-sm text-slate-300 focus:border-primary focus:outline-none appearance-none"
                                value={currency || 'INR'}
                                onChange={(e) => handleSpecChange('currency', e.target.value)}
                            >
                                {CURRENCIES.map(c => <option key={c.value} value={c.value}>{c.label}</option>)}
                            </select>
                            <ChevronDown className="absolute right-2 top-2.5 text-slate-500 pointer-events-none" size={16} />
                        </div>
                    </div>
                    <div className="flex flex-col gap-1.5">
                        <label className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Desc Length</label>
                        <input
                            type="text"
                            value={descLength || '15 to 25 words'}
                            onChange={(e) => handleSpecChange('descLength', e.target.value)}
                            className="w-full bg-slate-900 border border-slate-700 rounded p-2 text-sm text-slate-300 focus:border-primary focus:outline-none"
                        />
                    </div>
                </div>

                <div className="flex flex-col gap-1.5 flex-1">
                    <label className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Other Specs</label>
                    <textarea
                        className="w-full flex-1 bg-slate-900 border border-slate-700 rounded p-3 text-sm text-slate-300 focus:border-primary focus:outline-none resize-none placeholder:text-slate-600"
                        placeholder="Enter custom constraints..."
                        value={otherSpecs || ''}
                        onChange={(e) => handleSpecChange('otherSpecs', e.target.value)}
                    ></textarea>
                </div>
            </div>
        </div>
    );
};

export default CourseGeneralForm;
