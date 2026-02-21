import pandas as pd

def calculate_team_metrics(team_df):
    """Calculates the Psychological Safety Index based on Project Aristotle."""
    # Safety score balances cooperation (Agreeableness) against stress stability (10 - Neuroticism).
    safety_score = (team_df['Agreeableness'].mean() + (10 - team_df['Neuroticism'].mean())) / 2
    return round(safety_score, 1)

def get_belbin_role(row):
    """Maps Big Five personality traits to professional Belbin Team Roles."""
    if row['Openness'] > 8 and row['Extraversion'] > 7: 
        return "Plant (Creative)"
    if row['Extraversion'] > 8 and row['Conscientiousness'] > 6: 
        return "Shaper (Driver)"
    if row['Agreeableness'] > 8 and row['Extraversion'] > 6: 
        return "Resource Investigator"
    if row['Conscientiousness'] > 8 and row['Neuroticism'] < 4: 
        return "Implementer"
    if row['Agreeableness'] > 8 and row['Neuroticism'] < 5: 
        return "Teamworker"
    return "Specialist"

def prepare_heatmap_data(team_df, required_skills):
    """Prepares data for the Strategic Competency Matrix."""
    display_cols = required_skills if required_skills else ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism']
    
    heatmap_data = []
    for _, row in team_df.iterrows():
        row_data = {"Name": row['Name']}
        for col in display_cols:
            if col in required_skills:
                # Color intensity based on Years of Experience.
                row_data[col] = row['Years_Exp'] if row['Primary_Skill'] == col else 0
            else:
                row_data[col] = row.get(col, 0)
        heatmap_data.append(row_data)
    return pd.DataFrame(heatmap_data)