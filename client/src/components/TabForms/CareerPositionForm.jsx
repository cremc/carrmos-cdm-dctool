import React, { useState, useEffect } from 'react';
import { ChevronDown, Check } from 'lucide-react';
import SearchableDropdown from '../SearchableDropdown';
import {
    fetchIndustries,
    fetchIndustryBranches,
    fetchCurrencies
} from '../../utils/api';

const ROLE_TYPES = [
    { value: 'interns', label: 'Interns' },
    { value: 'entrylevel', label: 'Entry-level and Junior' },
    { value: 'midlevel', label: 'Mid-level' },
    { value: 'senior', label: 'Senior-level' },
    { value: 'executive', label: 'Executive-level' },
    { value: 'all', label: 'All levels' }
];

const CHECKBOX_OPTIONS = [
    { id: 'name', label: 'Name' },
    { id: 'description', label: 'Description' },
    { id: 'industry', label: 'Industry' },
    { id: 'industry_branch', label: 'Industry branch' },
    { id: 'salary_range', label: 'Annual Salary range in Lacs INR' },
    { id: 'employing_organizations', label: 'Employing organizations' },
    { id: 'salary_potential', label: 'Salary potential' },
    { id: 'lifestyle_potential', label: 'Lifestyle potential' },
    { id: 'career_growth_potential', label: 'Career growth opportunities' },
    { id: 'job_stability_potential', label: 'Job stability potential' },
    { id: 'travel_opportunities', label: 'Travel opportunities' },
    { id: 'work_life_balance', label: 'Work-life balance' },
    { id: 'abroad_opportunities', label: 'Settling down abroad opportunities' },
    { id: 'networking_potential', label: 'Networking potential' },
    { id: 'sedantariness', label: 'Amount of sedentariness expected' },
    { id: 'physical_load', label: 'Physical load expected' },
    { id: 'mental_load', label: 'Mental load expected' },
    { id: 'analytical_load', label: 'Analytical load expected' },
    { id: 'travel_expected', label: 'Amount of travel expected' },
    { id: 'sales_effort', label: 'Amount of sales effort expected' },
    { id: 'data_source', label: 'Data source' }
];

const DEFAULT_OTHER_SPECS = `Name should be the most common industry name along with role type in parentheses, for example Junior ML Engineer (entry level)
Description should be short and in the range of 15 to 25 words.
Annual Salary range should be in Lacs INR.
Give at least 5 examples, | separated, for types of employing organizations.
Possible values for Salary potential, Lifestyle potential, Career growth opportunities, Job stability potential, Travel opportunities, Work-life balance, Settling down abroad opportunities, Networking potential should be limited to the following four values: Unknown/Low/Medium/High
Possible values for Amount of sedentariness expected, Physical load expected, Mental load expected, Analytical load expected, Amount of travel expected, Amount of sales effort expected should be limited to the following four values: None/Low/Medium/High
Data source should be the top URL from where major info has been found.`;

const CareerPositionForm = ({ formData, onChange }) => {
    const [options, setOptions] = useState({
        industries: [],
        industryBranches: [],
        currencies: []
    });

    useEffect(() => {
        const loadOptions = async () => {
            try {
                const [industries, industryBranches, currencies] = await Promise.all([
                    fetchIndustries(),
                    fetchIndustryBranches(),
                    fetchCurrencies()
                ]);
                setOptions({
                    industries,
                    industryBranches,
                    currencies
                });
            } catch (error) {
                console.error("Error fetching dropdown options:", error);
            }
        };
        loadOptions();
    }, []);

    // Ensure nested state exists
    const {
        industry, industryBranch, roleType,
        selectedCheckboxes, descLength, currency, otherSpecs
    } = formData || {};

    // Filter branches based on selected industry
    const filteredBranches = industry
        ? options.industryBranches.filter(b => b.industryId === industry.value)
        : options.industryBranches;

    const handleDropdownChange = (field, option) => {
        const updates = { [field]: option };

        // Reset dependent fields
        if (field === 'industry') {
            updates.industryBranch = null;
        }

        onChange({
            ...formData,
            ...updates
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

    // Initialize default other specs if empty
    useEffect(() => {
        if (formData && !formData.otherSpecs) {
            onChange({
                ...formData,
                otherSpecs: DEFAULT_OTHER_SPECS
            });
        }
    }, []); // Run once on mount

    return (
        <div className="grid grid-cols-12 gap-6 h-full p-1">
            {/* Column 1: Dropdowns (25% - spanned as 3/12) */}
            <div className="col-span-3 flex flex-col gap-4 overflow-y-auto pr-2">
                <SearchableDropdown
                    label="Industry"
                    options={options.industries}
                    placeholder="Industry..."
                    value={industry}
                    onChange={(opt) => handleDropdownChange('industry', opt)}
                />

                <SearchableDropdown
                    label="Industry Branch"
                    options={filteredBranches}
                    placeholder="Industry Branch..."
                    value={industryBranch}
                    onChange={(opt) => handleDropdownChange('industryBranch', opt)}
                    disabled={!industry}
                />

                <SearchableDropdown
                    label="Role Type"
                    options={ROLE_TYPES}
                    placeholder="Role Type..."
                    value={roleType}
                    onChange={(opt) => handleDropdownChange('roleType', opt)}
                />
            </div>

            {/* Column 2: Checkboxes (42% - spanned as 5/12) */}
            <div className="col-span-5 flex flex-col gap-4 border-l border-r border-slate-800/50 px-4 overflow-y-auto">
                <div className="flex flex-col gap-3 mt-2 pb-2">
                    <div className="grid grid-cols-2 gap-x-2 gap-y-3">
                        {CHECKBOX_OPTIONS.map(opt => (
                            <label key={opt.id} className="flex items-center gap-2 cursor-pointer group w-full" title={opt.label}>
                                <div className={`
                                    w-4 h-4 rounded border flex items-center justify-center transition-colors shrink-0
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
                                <span className={`text-sm leading-tight text-left truncate flex-1 min-w-0 ${selectedCheckboxes?.[opt.id] ? 'text-slate-200' : 'text-slate-500'}`}>
                                    {opt.label}
                                </span>
                            </label>
                        ))}
                    </div>
                </div>
            </div>

            {/* Column 3: Specs (33% - spanned as 4/12) */}
            <div className="col-span-4 flex flex-col gap-4 pl-2 h-full">
                <div className="grid grid-cols-2 gap-2 shrink-0">
                    <div className="flex flex-col gap-1.5">
                        <SearchableDropdown
                            label="Currency"
                            options={options.currencies}
                            placeholder="Currency..."
                            value={options.currencies.find(c => c.value === (currency || 'INR')) || { value: 'INR', label: 'INR' }}
                            onChange={(opt) => handleSpecChange('currency', opt.value)}
                        />
                    </div>
                    <div className="flex flex-col gap-1.5">
                        <label className="text-xs font-semibold text-slate-500 uppercase tracking-wider">Desc Length</label>
                        <input
                            type="text"
                            value={descLength || '15 to 25 words'}
                            onChange={(e) => handleSpecChange('descLength', e.target.value)}
                            className="w-full bg-slate-900 border border-slate-700 rounded p-2 text-sm text-slate-300 focus:border-primary focus:outline-none"
                        />
                    </div>
                </div>

                <div className="flex flex-col gap-1.5 flex-1 mt-auto pb-4 relative">
                    <label className="text-xs font-semibold text-slate-500 uppercase tracking-wider block mb-1">Other Specs</label>
                    <div className="relative w-full h-[42px]">
                        <textarea
                            className="absolute top-0 left-0 w-full h-[42px] focus:h-[240px] focus:-top-[198px] z-10 focus:z-[60] bg-slate-900 border border-slate-700 rounded py-2 px-3 text-sm text-slate-300 focus:border-primary focus:outline-none resize-none placeholder:text-slate-500 transition-all duration-300 shadow-lg"
                            placeholder="Constraints..."
                            value={otherSpecs || ''}
                            onChange={(e) => handleSpecChange('otherSpecs', e.target.value)}
                        ></textarea>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default CareerPositionForm;
