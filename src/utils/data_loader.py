import pandas as pd
import os

def load_employee_data(filepath="data/raw_employees.csv"):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Data file not found at {filepath}. Run the generator script first!")
    
    df = pd.read_csv(filepath)
    # Ensure all Big Five columns are numeric
    cols = ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism']
    df[cols] = df[cols].apply(pd.to_numeric)
    return df