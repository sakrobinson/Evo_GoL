import numpy as np
import random

# main.py is set up with the genetic algorithm and necessary functions
def genetic_algorithm_with_top_n_tracking(population_size=10, num_generations=50, top_n=5):
    population = main.initialize_population(population_size)
    top_n_rulesets = []  # This will store tuples of (ruleset, score)

    for generation in range(num_generations):
        scores = [main.evaluate(individual) for individual in population]
        
        # Update top performers
        for individual, score in zip(population, scores):
            if len(top_n_rulesets) < top_n or score > top_n_rulesets[-1][1]:
                top_n_rulesets.append((individual, score))
                top_n_rulesets.sort(key=lambda x: x[1], reverse=True)  # Sort by score in descending order
                top_n_rulesets = top_n_rulesets[:top_n]  # Keep only top n performers

        # Proceed with selection, crossover, and mutation as before
        selected = main.tournament_selection(population, scores)
        offspring = []
        for i in range(0, population_size, 2):
            parent1, parent2 = selected[i], selected[i+1]
            child1, child2 = main.crossover(parent1, parent2, main.crossover_rate)
            offspring.append(main.mutate(child1, main.mutation_rate))
            offspring.append(main.mutate(child2, main.mutation_rate))
        population = offspring

    return top_n_rulesets

# In visualize.py or wherever you wish to use this
if __name__ == "__main__":
    top_n_rulesets = genetic_algorithm_with_top_n_tracking(top_n=5)
    for i, (ruleset, score) in enumerate(top_n_rulesets):
        print(f"Top {i+1} Ruleset with score {score}: {ruleset}")
        # You can now pass each ruleset to your visualization/animation function
