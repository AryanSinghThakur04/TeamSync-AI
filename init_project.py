# init_project.py
import os
import pandas as pd
import numpy as np

# Create folders if they don't exist
folders = ['data', 'src/engine', 'src/analysis', 'src/utils', 'app']
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    # Create empty __init__.py files so Python sees them as modules
    with open(os.path.join(folder, '__init__.py'), 'w') as f:
        pass

# Generate Sample Data
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia", 
         "Kevin", "Laura", "Mason", "Nora", "Oscar", "Paula", "Quinn", "Riley", "Sam", "Tara"]

data = {
    "Name": names,
    "Openness": np.random.randint(1, 11, 20),
    "Conscientiousness": np.random.randint(1, 11, 20),
    "Extraversion": np.random.randint(1, 11, 20),
    "Agreeableness": np.random.randint(1, 11, 20),
    "Neuroticism": np.random.randint(1, 11, 20),
}

pd.DataFrame(data).to_csv("data/raw_employees.csv", index=False)
print("✅ Project structure and data initialized!")