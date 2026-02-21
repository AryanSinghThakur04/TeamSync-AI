def identify_leader(team_df):
    """
    Identifies a 'Natural Leader' based on OB research:
    High Extraversion + High Conscientiousness.
    """
    # Calculate a leadership score
    team_df['Leader_Score'] = (team_df['Extraversion'] * 0.6) + (team_df['Conscientiousness'] * 0.4)
    
    # Get the person with the highest score
    leader = team_df.loc[team_df['Leader_Score'].idxmax()]
    return leader['Name'], leader['Leader_Score']