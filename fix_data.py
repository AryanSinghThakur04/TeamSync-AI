import pandas as pd
import numpy as np

# This ensures the data is perfectly formatted for Pandas
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

df = pd.DataFrame(data)
# index=False is crucial to avoid extra columns
df.to_csv("data/raw_employees.csv", index=False)
print("✅ CSV data has been cleaned and recreated!")