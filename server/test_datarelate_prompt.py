import os
import sys
import json
from dotenv import load_dotenv

load_dotenv()
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.pe_module.datarelate_service import pe_datarelate_service

def main():
    api_key_loaded = bool(os.getenv("GEMINI_API_KEY"))
    print(f"API Key Loaded: {api_key_loaded}")
    
    if not api_key_loaded:
        print("Using Mock mode because GEMINI_API_KEY is not set in environment.")

    print("\n" + "="*50)
    print("Testing Course General (CG): 'B.Tech Computer Science'")
    print("="*50)
    res_cg = pe_datarelate_service.run_engine({"label": "B.Tech Computer Science"}, "course_general")
    print(json.dumps(res_cg, indent=2))

    print("\n" + "="*50)
    print("Testing Career Position (CP): 'Software Engineer'")
    print("="*50)
    res_cp = pe_datarelate_service.run_engine({"label": "Software Engineer"}, "career_position")
    print(json.dumps(res_cp, indent=2))

if __name__ == "__main__":
    main()
