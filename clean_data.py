import pandas as pd
import numpy as np

# A clean, expanded pool of 30 employees
names = [f"Employee_{i}" for i in range(1, 31)]
skills = ["Python", "Django", "SQL", "Cloud", "DevOps", "Testing"]

data = {
    "Name": names,
    "Openness": np.random.randint(1, 11, 30),
    "Conscientiousness": np.random.randint(1, 11, 30),
    "Extraversion": np.random.randint(1, 11, 30),
    "Agreeableness": np.random.randint(1, 11, 30),
    "Neuroticism": np.random.randint(1, 11, 30),
    "Primary_Skill": [np.random.choice(skills) for _ in range(30)],
    "Years_Exp": np.random.randint(1, 15, 30)
}

df = pd.DataFrame(data)
# index=False ensures no ghost columns are created
df.to_csv("data/raw_employees.csv", index=False)
print("✅ Management-Grade CSV rebuilt successfully!")