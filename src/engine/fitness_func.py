def calculate_fitness(team_df, project_context="General"):
    # --- 1. PSYCHOLOGICAL SAFETY SCORE ---
    # High Agreeableness + Low Neuroticism = Safer environment for ideas
    safety_score = (team_df['Agreeableness'].mean() + (10 - team_df['Neuroticism'].mean())) / 2
    
    # --- 2. SKILL HYBRID CHECK ---
    # Ensure the team isn't just nice, but capable. 
    # Example: Penalize if no one has 'Python' skills for a dev project.
    unique_skills = len(team_df['Primary_Skill'].unique())
    skill_coverage = unique_skills / len(team_df)

    # --- 3. ROLE-BASED OPTIMIZATION ---
    role_weight = 0
    if project_context == "R&D (High Openness)":
        # Reward teams with high 'Openness' for research projects
        role_weight = team_df['Openness'].mean() * 2
    elif project_context == "Execution (High Conscientiousness)":
        # Reward 'Conscientiousness' for QA or deadline-heavy tasks
        role_weight = team_df['Conscientiousness'].mean() * 2

    # --- 4. THE "TOO MANY COOKS" PENALTY ---
    # From OB: Too many high-extraversion Alphas cause conflict
    alphas = team_df[team_df['Extraversion'] > 8]
    friction_penalty = 10 if len(alphas) > 2 else 0

    # Final Weighted Formula
    total_score = (safety_score * 3) + (skill_coverage * 10) + role_weight - friction_penalty
    return max(0, total_score)