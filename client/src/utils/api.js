import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

export const fetchAcademicLevels = async () => {
    const response = await axios.get(`${API_BASE_URL}/academics/academic_levels/`);
    return response.data.map(item => ({ value: item.academic_level_id, label: item.name }));
};

export const fetchDisciplineGroups = async () => {
    const response = await axios.get(`${API_BASE_URL}/academics/discipline_groups/`);
    return response.data.map(item => ({ value: item.discipline_group_id, label: item.name }));
};

export const fetchDisciplines = async () => {
    const response = await axios.get(`${API_BASE_URL}/academics/disciplines/`);
    return response.data.map(item => ({
        value: item.discipline_id,
        label: item.name,
        disciplineGroupId: item.discipline_group_id // Added for filtering
    }));
};

export const fetchCountries = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/general/countries/`);
        return response.data.map(item => ({ value: item.country_id, label: item.name }));

    }
    catch (error) {
        console.error("Error fetching countries:", error);
        return [];
    }

};

export const fetchProvinces = async () => {
    const response = await axios.get(`${API_BASE_URL}/general/provinces/`);
    return response.data.map(item => ({
        value: item.province_or_state_id,
        label: item.name,
        countryId: item.country_id // Added for filtering
    }));
};

export const fetchCurrencies = async () => {
    const response = await axios.get(`${API_BASE_URL}/finance/currencies/`);
    return response.data.map(item => ({ value: item.currency_code, label: item.currency_code }));
};

export const fetchInstitutionCategories = async () => {
    const response = await axios.get(`${API_BASE_URL}/institution/categories/`);
    return response.data.map(item => ({ value: item.institution_category_id, label: item.name }));
};

export const fetchInstitutions = async () => {
    const response = await axios.get(`${API_BASE_URL}/institution/institutions/`);
    return response.data.map(item => ({ value: item.institution_id, label: item.name }));
};

export const fetchIndustries = async () => {
    const response = await axios.get(`${API_BASE_URL}/career/industries/`);
    return response.data.map(item => ({ value: item.industry_id, label: item.industry_name }));
};

export const fetchIndustryBranches = async () => {
    const response = await axios.get(`${API_BASE_URL}/career/industry_branches/`);
    return response.data.map(item => ({
        value: item.industry_branch_id,
        label: item.name,
        industryId: item.industry_id // Added for filtering
    }));
};

export const createUser = async (userData) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/api/users/`, userData);
        return response.data;
    } catch (error) {
        console.error("Error creating user:", error);
        throw error;
    }
};
