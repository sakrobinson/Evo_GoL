import numpy as np
import random

# Parameters
population_size = 10 #individuals in the genetic population.
num_generations = 50
crossover_rate = 0.7
mutation_rate = 0.01
grid_size = 25

# Initialization
def initialize_population(population_size, grid_size):
    population = []
    for _ in range(population_size):
        # Generate a random ruleset
        ruleset = [random.randint(0, 1) for _ in range(9)]
        # Generate a random initial state
        initial_state = np.random.randint(2, size=(grid_size, grid_size))
        # Add the individual to the population
        population.append((ruleset, initial_state))
    return population

def get_neighbors(state, x, y):
    neighbors = state[np.ix_([(x-1)%state.shape[0], x, (x+1)%state.shape[0]], 
                             [(y-1)%state.shape[1], y, (y+1)%state.shape[1]])]
    return np.sum(neighbors) - state[x, y]

def step_game_of_life(state, ruleset):
    new_state = np.zeros_like(state)
    for x in range(state.shape[0]):
        for y in range(state.shape[1]):
            neighbors = get_neighbors(state, x, y)
            if state[x, y] == 1 and neighbors in ruleset['survive']:
                new_state[x, y] = 1
            elif state[x, y] == 0 and neighbors in ruleset['birth']:
                new_state[x, y] = 1
    return new_state

def simulate_game_of_life(initial_state, ruleset, steps=10):
    states = [initial_state]
    for _ in range(steps):
        new_state = step_game_of_life(states[-1], ruleset)
        states.append(new_state)
    return states[-1], states

def calculate_stability(states):
    unchanged_cells = np.sum(states[-1] == states[-2])
    total_cells = states[-1].size
    return unchanged_cells / total_cells

def calculate_complexity(states):
    changes = np.sum(np.abs(states[-1] - states[-2]))
    max_changes = states[-1].size
    return changes / max_changes

def calculate_diversity(states):
    alive_counts = [np.sum(state) for state in states]
    return np.var(alive_counts)

def evaluate(individual):
    # Unpack the individual into ruleset and initial_state
    ruleset, initial_state = individual
    # Convert individual to ruleset format
    ruleset = {'survive': [i for i in range(9) if ruleset[i] == 1], 'birth': [3]} # Simplified ruleset for GoL
    _, states = simulate_game_of_life(initial_state, ruleset, steps=100) # hard coded parameters for now, steps
    stability = calculate_stability(states)
    complexity = calculate_complexity(states)
    diversity = calculate_diversity(states)
    return (stability + complexity + diversity) / 3

def tournament_selection(population, scores, k=3):
    selection = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, scores)), k)
        tournament.sort(key=lambda x: x[1], reverse=True)
        selection.append(tournament[0][0])
    return selection

def crossover(parent1, parent2, crossover_rate):
    if random.random() < crossover_rate:
        # Separate the rulesets and initial states
        ruleset1, state1 = parent1
        ruleset2, state2 = parent2

        # Perform crossover on the rulesets
        point = random.randint(1, len(ruleset1)-2)
        child_ruleset1 = np.concatenate((ruleset1[:point], ruleset2[point:]))
        child_ruleset2 = np.concatenate((ruleset2[:point], ruleset1[point:]))

        # Combine the new rulesets with the original states to form the new individuals
        child1 = (child_ruleset1, state1)
        child2 = (child_ruleset2, state2)

        return child1, child2

    return parent1, parent2

def mutate(individual, mutation_rate):
    ruleset, state = individual
    for i in range(len(ruleset)):
        if random.random() < mutation_rate:
            ruleset[i] = 1 - ruleset[i]
    return (ruleset, state)


if __name__ == "__main__":
    def genetic_algorithm():
        population = initialize_population(population_size = population_size, grid_size = grid_size)
        best_score = -1
        best_individual = None
        for generation in range(num_generations):
            scores = [evaluate(individual) for individual in population]
            if max(scores) > best_score:
                best_index = scores.index(max(scores))
                best_score = scores[best_index]
                best_individual = population[best_index]
            selected = tournament_selection(population, scores)
            offspring = list()
            for i in range(0, population_size, 2):
                parent1, parent2 = selected[i], selected[i+1]
                child1, child2 = crossover(parent1, parent2, crossover_rate)
                offspring.append(mutate(child1, mutation_rate))
                offspring.append(mutate(child2, mutation_rate))
            population = offspring
        return best_individual, best_score

    best_ruleset, best_score = genetic_algorithm()
    print("Best Ruleset:", best_ruleset, "with score:", best_score)
