import React from 'react';
import { Search, Bell, Menu } from 'lucide-react';

const Header = () => {
    return (
        <header className="sticky top-0 z-50 flex items-center justify-between whitespace-nowrap border-b border-solid border-gray-200 dark:border-border-dark bg-white dark:bg-[#111418] px-6 py-3">
            {/* Left side (Title is in sidebar, so minimal here or breadcrumbs? Design shows just the right side mostly if sidebar is present) */}
            {/* The provided Dashboard HTML had the header spanning the full width including logo. 
                Since we have a Sidebar layout, this header sits to the right of the sidebar. 
                We will implement the Search and Right-side controls here. 
            */}

            <div className="flex items-center gap-4">
                {/* Search Bar - Hidden on small screens */}
                <label className="hidden md:flex flex-col min-w-40 !h-10 max-w-64">
                    <div className="flex w-full flex-1 items-stretch rounded-lg h-full">
                        <div className="text-slate-400 dark:text-[#9dabb8] flex border-none bg-slate-100 dark:bg-[#293038] items-center justify-center pl-4 rounded-l-lg border-r-0">
                            <Search size={20} />
                        </div>
                        <input
                            className="flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg rounded-l-none border-l-0 text-slate-900 dark:text-white focus:outline-0 focus:ring-0 border-none bg-slate-100 dark:bg-[#293038] focus:border-none h-full placeholder:text-slate-400 dark:placeholder:text-[#9dabb8] px-4 pl-2 text-sm font-normal leading-normal"
                            placeholder="Search data..."
                            defaultValue=""
                        />
                    </div>
                </label>
            </div>

            <div className="flex flex-1 justify-end gap-6 items-center">
                <div className="hidden md:flex items-center gap-6">
                    <a className="text-slate-600 dark:text-white text-sm font-medium leading-normal hover:text-primary transition-colors" href="#">Dashboard</a>
                    <a className="text-slate-600 dark:text-white text-sm font-medium leading-normal hover:text-primary transition-colors" href="#">Reports</a>
                    <a className="text-slate-600 dark:text-white text-sm font-medium leading-normal hover:text-primary transition-colors" href="#">Settings</a>
                </div>
                <div className="flex items-center gap-3 pl-3 border-l border-gray-200 dark:border-border-dark">
                    <button className="relative text-slate-500 hover:text-primary dark:text-white transition-colors">
                        <Bell size={24} />
                        <span className="absolute top-0 right-0 size-2 bg-red-500 rounded-full border-2 border-white dark:border-[#111418]"></span>
                    </button>
                    {/* Profile Picture Placeholder */}
                    <div
                        className="bg-center bg-no-repeat aspect-square bg-cover rounded-full size-9 ring-2 ring-white dark:ring-border-dark bg-slate-200"
                        style={{ backgroundImage: 'url("https://ui-avatars.com/api/?name=Ankur+Singh&background=0D8ABC&color=fff")' }}
                    ></div>
                </div>
            </div>
        </header>
    );
};

export default Header;
