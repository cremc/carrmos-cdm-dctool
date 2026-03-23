from typing import List, Dict, Any, Optional
import json
import re
import os
import ast
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel

def engineer_datarelate_prompt(input_data: Dict[str, Any], domain: str) -> str:
    """
    Engineers the prompt based on the user-provided txt file examples for data relate.
    """
    label = input_data.get('label', '')
    
    # Base schema instructions matching Model_fetched_data_structure.json
    schema_instruction = """
The requirements should be provided as a table or array of groups. A group of prerequisites can be a combination of cg+cp, or cg alone, or cp alone. Each group should contain at least one of the following:
i. A course general (CG) data: This should be the most common and most representative name of the course. A maximum of one data of cg type should be there in one group. If there is another (or more) alternative cg route for the same cp, then that cg+cp would have another group.
ii. A career position (CP) data: This should be the most common and most representative name of the career position. A maximum of one data of cp type should be there in one group. If there another (or more) alternative cp prerequisite for the same cg, then that cg+cp should form another group.
iii. One or more certification (Cert) data: This should be the most common and most representative name of the certification. More than one data of cert type can be there in one group. If there are two certs requirement, and if they are both required, they should be indicated as an AND join. And if they are two alternative certs requirements, they should be displayed as an OR join.
iv. One or more 'Others' data: An 'Others' data can represent many different types of data: Skills data, Subjects data, ET data and Others data. Each datatype should be grouped as a different stack of 'Others' data. A Group can have multiple 'Others' subgroups, one for skills, another for subjects, another for Entrance exams requirements, and yet another for other requirements not falling anywhere or not structured. There can be a maximum of four 'Others' subgroups within a Group, and minimum 0.

As mentioned above, the requirements output should be provided as an array of groups in json format.

Do not provide any other information outside the json object, as this data will be fed into a system that can only read jsons. 
The JSON output must have a top-level key "data" containing the array of groups, each with an "id" and "data" object containing "pathName", "cg", "cp", "certs" array, and "others" object.
For certifications, format as `[ { "type": "AND", "anded_certs": [ ... ] }, { "type": "OR", "ored_certs": [ ... ] } ]`.
For others, format as `{ "skills": [ ... ], "subjects": [ ... ], "ET": "...", "other_reqs": [ { "type": "AND", "anded_other_reqs": [...] }, { "type": "OR", "ored_other_reqs": [...] } ] }`.
    """

    if domain == 'course_general':
        prompt_str = f"""
You are an expert career counselor and academic advisor for the Indian education system and job market. 

Our current requirement is to counsel students from class 9 and above right upto students who have just completed their 12th grade exam. 
Their question is what are the different prerequisites (academic, work-experience, certifications, skills and other requirements) to become a/an {label}?
{schema_instruction}
        """
        
    elif domain == 'career_position':
        prompt_str = f"""
You are an expert career counselor and academic advisor for the Indian education system and job market. 

Our current requirement is to counsel students from class 9 and above right upto students who have just completed their 12th grade exam. 
Their question is what are the different prerequisites (academic, work-experience, certifications, skills and other requirements) to become a/an {label}?
{schema_instruction}
        """
        
    else:
        prompt_str = f"""
You are an expert career counselor and academic advisor for the Indian education system and job market.
The user is asking for related career and course information regarding: {label}.
{schema_instruction}
        """

    return prompt_str

class DataRelatePEService:
    def __init__(self):
        self.mock_mode = True 
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        if self.api_key:
            self.mock_mode = False
            self.llm = ChatGoogleGenerativeAI(google_api_key=self.api_key, model="gemini-flash-latest", temperature=0)
        else:
            print("GEMINI_API_KEY not found in environment variables. Defaulting to mock mode (DataRelate).")
            self.llm = None

    def run_engine(self, input_data: Dict[str, Any], domain: str, api_key: Optional[str] = None) -> List[Dict[str, Any]]:
        if api_key:
            try:
                self.llm = ChatGoogleGenerativeAI(google_api_key=api_key, model="gemini-flash-latest", temperature=0)
                self.mock_mode = False
            except Exception as e:
                print(f"Error initializing LLM with provided key: {e}")
                self.mock_mode = True

        if self.mock_mode:
            return self._get_mock_data(domain, input_data)

        try:
            prompt_str = engineer_datarelate_prompt(input_data, domain)
            response = self.llm.invoke(prompt_str)
            content = response.content
            
            if isinstance(content, list):
                texts = []
                for item in content:
                    if isinstance(item, dict) and "text" in item:
                        texts.append(item["text"])
                    elif isinstance(item, str):
                        texts.append(item)
                    else:
                        texts.append(str(item))
                content = "".join(texts)
            
            if "```json" in content:
                content = content.replace("```json", "").replace("```", "")
            elif "```" in content:
                content = content.replace("```", "")
                
            content = content.strip()
            
            parsed_json = None
            def try_parse(text):
                try: return json.loads(text) 
                except: pass
                try: return ast.literal_eval(text) 
                except: pass
                try:
                    m = re.search(r'\{.*\}', text, re.DOTALL)
                    if m: return json.loads(m.group(0))
                except: pass
                
                # Also try array regex since the expected top level is {'data': [...]} but models sometimes just return [...]
                try:
                    m = re.search(r'\[.*\]', text, re.DOTALL)
                    if m: return json.loads(m.group(0))
                except: pass
                
                return None

            parsed_json = try_parse(content)
            
            # Save for debugging
            if parsed_json:
                with open("output.json", "w", encoding="utf-8") as f:
                    json.dump(parsed_json, f, indent=4)

            
            if isinstance(parsed_json, list):
                # The model returned an array directly as requested in the instructions
                return parsed_json
            elif parsed_json and "data" in parsed_json and isinstance(parsed_json["data"], list):
                return parsed_json["data"]
            else:
                print(f"Unexpected JSON structure: {parsed_json.keys() if isinstance(parsed_json, dict) else parsed_json}")
                return self._get_mock_data(domain, input_data)
                
        except Exception as e:
            print(f"Error calling Gemini API: {e}")
            return self._get_mock_data(domain, input_data)

    def _get_mock_data(self, domain: str, input_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        label = input_data.get("label", "Unknown")
        return [
            {
                "id": "mock-group-1",
                "data": {
                    "pathName": f"Path for {label}",
                    "cg": {
                        "id": "cg1",
                        "label": f"Bachelors degree related to {label}"
                    },
                    "cp": {
                        "id": "cp1",
                        "label": label,
                        "exp": "1-3 years"
                    },
                    "certs": [
                        {
                            "type": "AND",
                            "anded_certs": [{"id": "cert1", "label": "Relevant Cert 1"}]
                        }
                    ],
                    "others": {
                        "skills": [{"id": "sk1", "skill_category": "General", "skill_subcategory": "Mock Skill"}],
                        "subjects": [],
                        "ET": "none",
                        "other_reqs": []
                    }
                }
            }
        ]

pe_datarelate_service = DataRelatePEService()
