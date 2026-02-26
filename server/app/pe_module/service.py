from typing import List, Dict, Any, Optional
import json
import re
import os
import ast
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'prompt_config.json')

def load_prompt_config() -> Dict[str, str]:
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as f:
            return json.load(f)
    return {
        "header": "You are a responsible and veteran career counsellor.",
        "footer": "The output MUST be a JSON object with a single key 'data', which is a list of dictionaries.\nEach dictionary should represent a record, with the keys in each dictionary corresponding to the keys mentioned above.\n\nExample format:\n{\n    \"data\": [\n        { \"name\": \"B.Tech CS\", \"description\": \"...\", \"duration\": \"4 Years\", \"rigour\": \"...\", \"tuition\": \"...\", \"career\": \"...\", \"course group\": \"...\", \"course domain\": \"...\" }\n    ]\n}\nRETURN ONLY JSON. NO MARKDOWN."
    }

def save_prompt_config(header: str, footer: str):
    with open(CONFIG_PATH, 'w') as f:
        json.dump({"header": header, "footer": footer}, f, indent=4)

# Define Pydantic models for structured output
class GenericOutput(BaseModel):
    data: List[Dict[str, Any]] = Field(description="List of records compatible with the destination table")

def engineer_prompt(input_data: Dict[str, Any], domain: str) -> str:
    """
    Engineers the prompt depending on the input_data and domain.
    """
    prompt_str = ""
    
    # Helper to safely get label or value
    def get_label(field):
        return input_data.get(field, {}).get('label', '') if input_data.get(field) else 'Any'

    def get_value(field):
         return input_data.get(field, {}).get('value', '') if input_data.get(field) else 'Any'
        
    desc_length = input_data.get('descLength', '15 to 25 words')
    currency = input_data.get('currency', 'INR')

    config = load_prompt_config()
    header = config.get("header", "You are a responsible and veteran career counsellor.")
    footer = config.get("footer", "")

    if domain == "course_general":
        # Engineers the prompt for General Course inquiries
        prompt_str = f"""
        {header} You are expected to provide career-related advice in '{domain}' domain to be consumed by aspiring students.
        Currently you are required to get all the courses available in {get_label('country')} ({get_label('state')} state) corresponding to the following fields:
            academic level: {get_label('academicLevel')},
            discipline group: {get_label('disciplineGroup')},
            discipline: {get_label('discipline')}
        
        The following parameters are required for each course retrieved:
        1. Name of the course (key: "name")
        2. Short description strictly within {desc_length} (key: "description")
        3. Course duration (key: "duration")
        4. Rigor and challenges (15 to 25 words) (key: "rigour")
        5. Course tuition cost range in {currency} (key: "tuition")
        6. Career prospects after completion strictly within {desc_length} (key: "career")
        7. Course group  (base course name, e.g. B.Tech, M.B.A.) (key: "group1")
        8. Course domain (domain name, e.g. Veterinary science) (key: "group2")

        {footer}
        """

    elif domain == "course_specific":
        # Engineers the prompt for Specific Course inquiries (with Institution context)
        prompt_str = f"""
        {header}
        You are expected to provide career-related advice in '{domain}' domain for specific institutions.
        
        Context:
        - Country: {get_label('country')}
        - State/Province: {get_label('state')}
        - Academic Level: {get_label('academicLevel')}
        - Discipline Group: {get_label('disciplineGroup')}
        - Discipline: {get_label('discipline')}
        - Institution Category: {get_label('institutionCategory')}
        - Institution: {get_label('institution')}
        
        Please retrieve detailed course information matching these criteria.
        
        The following parameters are required for each course retrieved:
        1. Course Name (key: "name")
        2. Description (within {desc_length}) (key: "description")
        3. Course General info (key: "course_general")
        4. Institution Name (key: "institution_name")
        5. Admission Criteria (key: "admission_criteria")
        6. Course Type (key: "course_type")
        7. Tuition Cost (in {currency}) (key: "tuition_cost")
        8. Course Prep Advice (key: "course_prep_advice")
        9. Degree Awarded (key: "degree_awarded")
        10. Certified By (key: "certified_by")
        11. Conducted By (key: "conducted_by")
        12. Course Duration (key: "course_duration")
        13. Career Prospect (key: "career_prospect")
        14. Rigour (key: "rigour")
        15. Activeness Scale (1-10) (key: "activeness_scale")
        16. Physical Load Scale (1-10) (key: "physical_load_scale")
        17. Mental Load Scale (1-10) (key: "mental_load_scale")
        18. Analytical Load Scale (1-10) (key: "analytical_load_scale")

        {footer}
        """
        
    elif domain == "others":
        # Engineers the prompt for "Others" (free-text requirement)
        query = input_data.get('query', '')
        prompt_str = f"""
        {header}
        The user has a specific requirement described as follows:
        "{query}"

        Please identify the key intent and providing the relevant information in a structured format.
        Focus on providing concrete data points such as names, descriptions, or specific values where applicable.
        
        {footer}
        """
        
    else:
        # Default prompt construction for other domains
        prompt_str = f"""
        You are a synthetic data generator.
        Generate 2 realistic records for the domain '{domain}'.
        
        Input parameters/context: {json.dumps(input_data)}
        
        {footer}
        """
        
    return prompt_str


class PEService:
    def __init__(self):
        # Check for GEMINI_API_KEY
        self.mock_mode = True 
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        if self.api_key:
            self.mock_mode = False
            # Initialize Gemini Pro
            self.llm = ChatGoogleGenerativeAI(google_api_key=self.api_key, model="gemini-flash-latest", temperature=0)
        else:
            print("GEMINI_API_KEY not found in environment variables. Defaulting to mock mode.")
            self.llm = None

    def run_engine(self, input_data: Dict[str, Any], domain: str, api_key: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Engineers the prompt, invokes the LLM (or mock), and returns structured data.
        """
        
        # Allow overriding/providing API key per request
        if api_key:
            try:
                # Re-initialize LLM with provided key
                self.llm = ChatGoogleGenerativeAI(google_api_key=api_key, model="gemini-flash-latest", temperature=0)
                self.mock_mode = False
            except Exception as e:
                print(f"Error initializing LLM with provided key: {e}")
                self.mock_mode = True

        if self.mock_mode:
            return self._get_mock_data(domain, input_data)

        # Real LangChain implementation for Gemini
        try:
            prompt_str = engineer_prompt(input_data, domain)
            print (f"The prompt is: \n {prompt_str}")
            response = self.llm.invoke(prompt_str)
            print (f"The response is: \n {response}")
            content = response.content
            
            # Handle case where content is a list (e.g. multi-part response)
            if isinstance(content, list):
                content = "".join([str(item) for item in content])
            
            # Clean up potential markdown code blocks
            if "```json" in content:
                content = content.replace("```json", "").replace("```", "")
            elif "```" in content:
                content = content.replace("```", "")
                
            content = content.strip()
            
            parsed_json = None
            
            def try_parse(text):
                # 1. Try JSON
                try: 
                    return json.loads(text) 
                except: 
                    pass
                # 2. Try Python Literal (for single quoted dicts)
                try: 
                    return ast.literal_eval(text) 
                except: 
                    pass
                # 3. Try Regex extraction for JSON
                try:
                    m = re.search(r'\{.*\}', text, re.DOTALL)
                    if m: return json.loads(m.group(0))
                except:
                    pass
                return None

            parsed_json = try_parse(content)
            
            # Logic to unwrap nested structures common in Gemini content responses
            # Case 1: List of blocks e.g. [{'type': 'text', 'text': '...'}]
            if isinstance(parsed_json, list) and len(parsed_json) > 0 and isinstance(parsed_json[0], dict) and 'text' in parsed_json[0]:
                 result = try_parse(parsed_json[0]['text'])
                 if result: parsed_json = result
            
            # Case 2: Dict wrapper e.g. {'type': 'text', 'text': '...'}
            elif isinstance(parsed_json, dict) and 'text' in parsed_json and 'data' not in parsed_json:
                 result = try_parse(parsed_json['text'])
                 if result: parsed_json = result
            
            if parsed_json and "data" in parsed_json and isinstance(parsed_json["data"], list):
                return parsed_json["data"]
            else:
                print(f"Unexpected JSON structure: {parsed_json.keys() if isinstance(parsed_json, dict) else parsed_json}")
                return self._get_mock_data(domain, input_data)
                
        except Exception as e:
            print(f"Error calling Gemini API: {e}")
            return self._get_mock_data(domain, input_data)

    def _get_mock_data(self, domain: str, input_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Returns dummy data matching the table structure for testing.
        """
        print(f"Generating mock data for domain: {domain}")
        
        if domain == "course_general":
            return [
                {
                    "name": "B.Tech Computer Science",
                    "description": "Foundational course in CS.",
                    "duration": "4 Years",
                    "rigour": "High",
                    "tuition": "10-15 Lakhs",
                    "career": "Software Engineer",
                    "Course group": "B.Tech",
                    "Course domain": "Computer Science"
                }
            ]
        elif domain == "course_specific":
            return [
                {
                    "name": "B.Tech CS - IIT Bombay",
                    "description": "Specific program details...",
                    "course_general": "Engineering",
                    "institution_name": "IIT Bombay",
                    "admission_criteria": "JEE Advanced",
                    "course_type": "Degree",
                    "tuition_cost": "8 Lakhs",
                    "course_prep_advice": "Focus heavily on Math/Physics",
                    "degree_awarded": "B.Tech",
                    "certified_by": "IITB",
                    "conducted_by": "CSE Dept",
                    "course_duration": "4 Years",
                    "career_prospect": "Top Tier Tech Companies",
                    "rigour": "Very High",
                    "activeness_scale": "Mid",
                    "physical_load_scale": "Low",
                    "mental_load_scale": "High",
                    "analytical_load_scale": "High"
                }
            ]
            

            
        elif domain == "others":
            return [
                {
                    "name": "Sample Result 1",
                    "description": "This is a mock result for the custom query.",
                    "category": "Mock Data",
                    "details": "Details about the result."
                },
                {
                    "name": "Sample Result 2",
                    "description": "Another mock result based on the query.",
                    "category": "Mock Data",
                    "details": "More details."
                }
            ]
            
        return [{"info": "No specific mock data for this domain yet"}]

pe_service = PEService()
