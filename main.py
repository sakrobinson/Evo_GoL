import numpy as np
import random

# Parameters
population_size = 10
num_generations = 50
crossover_rate = 0.7
mutation_rate = 0.01

# Initialization
def initialize_population(population_size):
    return [np.random.randint(2, size=9) for _ in range(population_size)]

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
    # Convert individual to ruleset format
    ruleset = {'survive': [i for i in range(9) if individual[i] == 1], 'birth': [3]} # Simplified ruleset
    initial_state = np.random.randint(2, size=(10, 10))
    _, states = simulate_game_of_life(initial_state, ruleset, steps=10)
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
        point = random.randint(1, len(parent1)-2)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1, parent2

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

def genetic_algorithm():
    population = initialize_population(population_size)
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
