import React, { useState } from 'react';
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

const INSTITUTION_CATEGORIES = [
    { value: 'premier_private', label: 'Premier Private' },
    { value: 'premier_public', label: 'Premier Public' },
    { value: 'private', label: 'Private' },
    { value: 'public', label: 'Public' }
];

const INSTITUTIONS = [
    { value: 'iit_bombay', label: 'IIT Bombay' },
    { value: 'bits_pilani', label: 'BITS Pilani' },
    { value: 'manipal', label: 'Manipal University' },
    { value: 'vit', label: 'VIT Vellore' }
];

const CURRENCIES = [
    { value: 'INR', label: 'INR' },
    { value: 'USD', label: 'USD' },
    { value: 'GBP', label: 'GBP' },
    { value: 'EUR', label: 'EUR' }
];

const CHECKBOX_OPTIONS_GENERAL = [
    { id: 'name', label: 'Name' },
    { id: 'description', label: 'Description' },
    { id: 'duration', label: 'Course duration' },
    { id: 'rigour', label: 'Rigour and challenges' },
    { id: 'tuition', label: 'Course tuition cost range' },
    { id: 'career', label: 'Career prospects after completion' },
    { id: 'group1', label: 'Course Group 1 (Academic level + DG)' },
    { id: 'group2', label: 'Course Group 2 (Discipline)' }
];

const CHECKBOX_OPTIONS_SPECIFIC = [
    { id: 'description', label: 'Description' },
    { id: 'cert_name', label: 'Final name of the certificate provided' },
    { id: 'admission', label: 'Admission criteria' },
    { id: 'cost', label: 'Cost range' },
    { id: 'advice', label: 'Course preparation advice' },
    { id: 'cert_by', label: 'Certificate issued by (institution name)' },
    { id: 'duration', label: 'Course duration' },
    { id: 'rigour', label: 'Rigour and challenges' },
    { id: 'career', label: 'Career prospect on completion' }
];

const CourseForm = ({ formData, onChange }) => {
    // Helper to safely access nested state if it hadn't initialized (though it should have from parent)
    const {
        academicLevel, disciplineGroup, discipline, country, state,
        institutionCategory, institution, courseType, selectedCheckboxes
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

    const handleCourseTypeChange = (value) => {
        onChange({
            ...formData,
            courseType: value
        })
    }

    const currentCheckboxOptions = courseType === 'general' ? CHECKBOX_OPTIONS_GENERAL : CHECKBOX_OPTIONS_SPECIFIC;

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

                <SearchableDropdown
                    label="Institution Category"
                    options={INSTITUTION_CATEGORIES}
                    placeholder="Institution Category..."
                    value={institutionCategory}
                    onChange={(opt) => handleDropdownChange('institutionCategory', opt)}
                />
                <SearchableDropdown
                    label="Institution"
                    options={INSTITUTIONS}
                    placeholder="Institution..."
                    value={institution}
                    onChange={(opt) => handleDropdownChange('institution', opt)}
                />
                {/* <SearchableDropdown label="Course Type" options={COURSE_TYPES} value={{ value: courseType, label: courseType === 'general' ? 'Course General' : 'Course Specific' }} onChange={(opt) => setCourseType(opt.value)} /> */}
                {/* Note: In the UI image, Course Type selector seems to be in the second column or implicit. 
                    The requirement says: "For course type". I will put it here as per req. 
                    But later req says: "Labels and input fields for Second column... Search course type".
                    I will place it in Col 2 top as per "Search course type" requirement for Col 2.
                */}
            </div>

            {/* Column 2: Checkboxes (30% - spanned as 4/12) */}
            <div className="col-span-4 flex flex-col gap-4 border-l border-r border-slate-800/50 px-4">
                {/* Course Type Selector - moved here per "Search course type" in Col 2 req */}
                <div className="flex flex-col gap-1.5">
                    <label className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Extraction Targets</label>
                    {/* Simplified dropdown for type */}
                    <div className="relative">
                        <select
                            className="w-full bg-slate-900 border border-slate-700 rounded p-2 text-sm text-slate-300 focus:border-primary focus:outline-none appearance-none"
                            value={courseType}
                            onChange={(e) => handleCourseTypeChange(e.target.value)}
                        >
                            <option value="general">Course General</option>
                            <option value="specific">Course Specific</option>
                        </select>
                        <ChevronDown className="absolute right-2 top-2.5 text-slate-500 pointer-events-none" size={16} />
                    </div>
                </div>

                <div className="flex flex-col gap-3 mt-2">
                    <div className="grid grid-cols-2 gap-x-2 gap-y-3">
                        {currentCheckboxOptions.map(opt => (
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
                            <select className="w-full bg-slate-900 border border-slate-700 rounded p-2 text-sm text-slate-300 focus:border-primary focus:outline-none appearance-none">
                                {CURRENCIES.map(c => <option key={c.value} value={c.value}>{c.label}</option>)}
                            </select>
                            <ChevronDown className="absolute right-2 top-2.5 text-slate-500 pointer-events-none" size={16} />
                        </div>
                    </div>
                    <div className="flex flex-col gap-1.5">
                        <label className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Desc Length</label>
                        <input type="text" defaultValue="15 to 25 words" className="w-full bg-slate-900 border border-slate-700 rounded p-2 text-sm text-slate-300 focus:border-primary focus:outline-none" />
                    </div>
                </div>

                <div className="flex flex-col gap-1.5 flex-1">
                    <label className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Other Specs</label>
                    <textarea
                        className="w-full flex-1 bg-slate-900 border border-slate-700 rounded p-3 text-sm text-slate-300 focus:border-primary focus:outline-none resize-none placeholder:text-slate-600"
                        placeholder="Enter custom constraints..."
                    ></textarea>
                </div>
            </div>
        </div>
    );
};

export default CourseForm;
