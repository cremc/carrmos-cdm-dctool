import React from 'react';

const OthersForm = ({ value, onChange, renderActionButtons, onFocusSpecs }) => {
    return (
        <div className="h-full flex flex-col p-1">
            <label className="text-xs font-semibold text-slate-500 uppercase tracking-wider block mb-1">Describe the requirement</label>
            <textarea
                value={value || ''}
                onChange={(e) => onChange(e.target.value)}
                onFocus={onFocusSpecs}
                className="w-full flex-1 bg-slate-900 border border-slate-700 rounded p-4 text-sm text-slate-300 focus:border-primary focus:outline-none resize-none placeholder:text-slate-600 leading-relaxed"
                placeholder="Describe what you are looking for. Provide as much detail as possible. The scope of your search should be limited to the following.
                            Academic level, Stream, Discipline Group, Discipline,
                            Course General, Course Specific, 
                            Core subjects, skills and subskills,
                            Industries, Industry branches,
                            Career positions and their requirements,
                            Institutions, Institution categories, Entrance exams, 
                            Course duration, Tuition cost range, Financial aid, 
                            Career prospects after completion"
            ></textarea>
            {renderActionButtons && renderActionButtons()}
        </div>
    );
};

export default OthersForm;
