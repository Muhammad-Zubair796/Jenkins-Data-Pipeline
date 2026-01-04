import os
import sys

def clean_data():
    # Get the environment name from Jenkins
    env_name = os.getenv("APP_ENV", "Unknown")
    
    print(f"--- Starting Data Cleaning Process in {env_name} environment ---")
    data = ["  messy_data  ", "NLP_MODEL_v1", "  2026_records  "]
    cleaned = [item.strip().lower() for item in data]
    print(f"Original: {data}")
    print(f"Cleaned: {cleaned}")
    print("--- Process Completed Successfully ---")

if __name__ == "__main__":
    clean_data()
