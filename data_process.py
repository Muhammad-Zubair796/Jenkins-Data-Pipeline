import sys

def clean_data():
    print("--- Starting Data Cleaning Process ---")
    data = ["  messy_data  ", "NLP_MODEL_v1", "  2026_records  "]
    cleaned = [item.strip().lower() for item in data]
    print(f"Original: {data}")
    print(f"Cleaned: {cleaned}")
    print("--- Process Completed Successfully ---")

if __name__ == "__main__":
    clean_data()
