import sys
import os
import json
from dotenv import load_dotenv

# Add current directory to path so we can import app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load env from app/.env
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app", ".env")
load_dotenv(env_path)

print(f"Loading env from: {env_path}")
print(f"GEMINI_API_KEY present: {'GEMINI_API_KEY' in os.environ}")

try:
    from app.pe_module.service import pe_service
    
    test_input = {"discipline": "Computer Science", "level": "Undergraduate"}
    domain = "course"

    print(f"\nRunning Gemini verification for domain '{domain}' with input: {test_input}")
    print("Waiting for response (this may take a few seconds)...")
    
    # We rely on the internal API key check
    result = pe_service.run_engine(test_input, domain)
    
    print("\n--- Result Received ---")
    print(json.dumps(result, indent=2))
    
    if pe_service.mock_mode:
        print("\n[WARNING] Service ran in MOCK MODE. Check API key.")
    else:
        print("\n[SUCCESS] Service ran in REAL MODE (Gemini).")

except ImportError as e:
    print(f"Import Error: {e}")
    print("Make sure requirements are installed and you are running from the 'server' directory.")
except Exception as e:
    import traceback
    print(f"Execution Error: {e}")
    traceback.print_exc()
