import pygad
import pandas as pd
import numpy as np
from .fitness_func import calculate_fitness

class TeamOptimizer:
    def __init__(self, df, team_size):
        self.df = df
        self.team_size = team_size
        self.num_employees = len(df)

    def fitness_wrapper(self, ga_instance, solution, solution_idx):
        # The GA gives us a list of indices (the 'solution')
        # We select those rows from our dataframe
        selected_indices = [int(i) for i in solution]
        
        # Penalty for duplicate members in a team
        if len(set(selected_indices)) != self.team_size:
            return 0
            
        team_df = self.df.iloc[selected_indices]
        return calculate_fitness(team_df)

    def run(self):
        # Genetic Algorithm Parameters
        ga_instance = pygad.GA(
            num_generations=50,
            num_parents_mating=5,
            fitness_func=self.fitness_wrapper,
            sol_per_pop=20,
            num_genes=self.team_size,
            gene_space=range(self.num_employees),
            gene_type=int,
            mutation_percent_genes=20
        )

        ga_instance.run()
        solution, solution_fitness, solution_idx = ga_instance.best_solution()
        return self.df.iloc[[int(i) for i in solution]]