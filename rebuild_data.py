import pandas as pd
import numpy as np
import os

if not os.path.exists('data'):
    os.makedirs('data')

names = [
    "Arjun Singh", "Priya Sharma", "Aarav Thakur", "Ishani Verma", "Siddharth Das", 
    "Ananya Iyer", "Vikram Malhotra", "Sanya Gupta", "Rohan Mehta", "Kavya Nair",
    "Aditya Joshi", "Meera Reddy", "Kabir Bansal", "Zoya Khan", "Ishaan Gill",
    "Riya Kapoor", "Dev Patel", "Myra Saxena", "Sahil Mishra", "Tanya Roy"
]

skills_pool = ["Python", "Django", "SQL", "Cloud Computing", "DevOps", "Testing", "React", "Data Science"]

data = {
    "Name": names,
    "Openness": np.random.randint(1, 11, len(names)),
    "Conscientiousness": np.random.randint(1, 11, len(names)),
    "Extraversion": np.random.randint(1, 11, len(names)),
    "Agreeableness": np.random.randint(1, 11, len(names)),
    "Neuroticism": np.random.randint(1, 11, len(names)),
    "Primary_Skill": [np.random.choice(skills_pool) for _ in range(len(names))],
    "Years_Exp": np.random.randint(1, 15, len(names)),
    "Annual_Salary": np.random.randint(50000, 150000, len(names)), # New: Cost Metric
    "Past_Performance": np.random.uniform(3.0, 5.0, len(names)).round(1)
}

df = pd.DataFrame(data)
df.to_csv("data/raw_employees.csv", index=False)
print("✅ Advanced Management Database Created!")