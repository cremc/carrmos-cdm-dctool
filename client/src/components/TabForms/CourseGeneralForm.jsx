import React, { useState, useEffect } from 'react';
import { ChevronDown, Check } from 'lucide-react';
import SearchableDropdown from '../SearchableDropdown';
import {
    fetchAcademicLevels,
    fetchDisciplineGroups,
    fetchDisciplines,
    fetchCountries,
    fetchProvinces,
    fetchCurrencies
} from '../../utils/api';

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

const CourseGeneralForm = ({ formData, onChange, renderActionButtons, onFocusSpecs }) => {
    const [options, setOptions] = useState({
        academicLevels: [],
        disciplineGroups: [],
        disciplines: [],
        countries: [],
        states: [],
        currencies: []
    });

    useEffect(() => {
        const loadOptions = async () => {
            try {
                const [academicLevels, disciplineGroups, disciplines, countries, states, currencies] = await Promise.all([
                    fetchAcademicLevels(),
                    fetchDisciplineGroups(),
                    fetchDisciplines(),
                    fetchCountries(),
                    fetchProvinces(),
                    fetchCurrencies()
                ]);
                setOptions({
                    academicLevels,
                    disciplineGroups,
                    disciplines,
                    countries,
                    states,
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
        academicLevel, disciplineGroup, discipline, country, state, selectedCheckboxes,
        descLength, currency, otherSpecs
    } = formData || {};

    // Filter disciplines based on selected group
    const filteredDisciplines = disciplineGroup
        ? options.disciplines.filter(d => d.disciplineGroupId === disciplineGroup.value)
        : options.disciplines;

    // Filter states based on selected country
    const filteredStates = country
        ? options.states.filter(s => s.countryId === country.value)
        : options.states;

    const handleDropdownChange = (field, option) => {
        const updates = { [field]: option };

        // Reset dependent fields
        if (field === 'disciplineGroup') {
            updates.discipline = null;
        }
        if (field === 'country') {
            updates.state = null;
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

    return (
        <div className="grid grid-cols-12 gap-6 h-full p-1">
            {/* Column 1: Dropdowns (25% - spanned as 3/12) */}
            <div className="col-span-3 flex flex-col gap-4 overflow-y-auto pr-2">
                <SearchableDropdown
                    label="Academic Level"
                    options={options.academicLevels}
                    placeholder="Academic Level..."
                    value={academicLevel}
                    onChange={(opt) => handleDropdownChange('academicLevel', opt)}
                />

                <div className="flex gap-2">
                    <div className="flex-1">
                        <SearchableDropdown
                            label="Discipline Group"
                            options={options.disciplineGroups}
                            placeholder="Discipline Group..."
                            value={disciplineGroup}
                            onChange={(opt) => handleDropdownChange('disciplineGroup', opt)}
                        />
                    </div>
                </div>

                <SearchableDropdown
                    label="Discipline"
                    options={filteredDisciplines}
                    placeholder="Discipline..."
                    value={discipline}
                    onChange={(opt) => handleDropdownChange('discipline', opt)}
                    disabled={!disciplineGroup}
                />

                <div className="grid grid-cols-2 gap-2">
                    <SearchableDropdown
                        label="Country"
                        options={options.countries}
                        placeholder="Country..."
                        value={country}
                        onChange={(opt) => handleDropdownChange('country', opt)}
                    />
                    <SearchableDropdown
                        label="State/Prov"
                        options={filteredStates}
                        placeholder="State/Prov..."
                        value={state}
                        onChange={(opt) => handleDropdownChange('state', opt)}
                        disabled={!country}
                    />
                </div>
            </div>

            {/* Column 2: Checkboxes (42% - spanned as 5/12) */}
            <div className="col-span-5 flex flex-col gap-4 border-l border-r border-slate-800/50 px-4">
                <div className="flex flex-col gap-3 mt-2">
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
                                <span
                                    className={`text-sm leading-tight text-left truncate flex-1 min-w-0 ${selectedCheckboxes?.[opt.id] ? 'text-slate-200' : 'text-slate-500'}`}
                                >
                                    {opt.label}
                                </span>
                            </label>
                        ))}
                    </div>
                </div>
            </div>

            {/* Column 3: Specs (33% - spanned as 4/12) */}
            <div className="col-span-4 flex flex-col gap-4 pl-2">
                <div className="grid grid-cols-2 gap-2">
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
                            className="absolute top-0 left-0 w-full h-[42px] focus:h-[240px] focus:-top-[198px] z-10 focus:z-[60] bg-slate-900 border border-slate-700 rounded py-2 px-3 text-sm text-slate-500 focus:text-slate-300 focus:border-primary focus:outline-none resize-none placeholder:text-slate-600 transition-all duration-300 shadow-lg"
                            placeholder="Constraints..."
                            value={otherSpecs || ''}
                            onChange={(e) => handleSpecChange('otherSpecs', e.target.value)}
                            onFocus={onFocusSpecs}
                        ></textarea>
                    </div>
                </div>

                {renderActionButtons && renderActionButtons()}
            </div>
        </div>
    );
};

export default CourseGeneralForm;
