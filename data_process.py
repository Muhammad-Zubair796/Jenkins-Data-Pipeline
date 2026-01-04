import os
import sys

def clean_data():
    env_name = os.getenv("APP_ENV", "Unknown")
    print(f"--- Starting Data Cleaning Process in {env_name} ---")
    
    data = ["  messy_data  ", "NLP_MODEL_v1", "  2026_records  "]
    cleaned = [item.strip().lower() for item in data]
    
    # NEW: Simple Validation Test
    for item in cleaned:
        if any(char.isupper() for char in item) or item.startswith(" ") or item.endswith(" "):
            print(f"ERROR: Data validation failed for item: {item}")
            sys.exit(1) # This tells Jenkins the script FAILED
            
    print(f"Cleaned Data: {cleaned}")
    print("--- Data Validation Passed! ---")

if __name__ == "__main__":
    clean_data()
