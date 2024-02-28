# EvoGol: Genetic Algorithm for Game of Life


This repository contains a Python script that uses a genetic algorithm to evolve rulesets for the Game of Life. The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.

## Files

- `main.py`: This is the main script that contains the genetic algorithm and the Game of Life simulation.

## How it works

The script uses a genetic algorithm to evolve rulesets for the Game of Life. The genetic algorithm uses a population of individuals, where each individual is a potential solution (ruleset) to the problem. The algorithm evolves the population over a number of generations through the processes of selection, crossover (recombination), and mutation.

The Game of Life simulation uses the evolved ruleset to simulate the Game of Life on a grid. The simulation steps through a number of generations, applying the ruleset to determine the state of each cell in the grid.

The fitness of each individual (ruleset) is determined by evaluating the stability, complexity, and diversity of the Game of Life simulation that it produces.

## Usage

To run the script, simply execute the `run.py` file:

```bash
python run.py
```

The script will output the best ruleset it found and its score.

## Parameters

The script uses the following parameters, stored in main.py for now:

- `population_size`: The number of individuals in the genetic population.
- `num_generations`: The number of generations to evolve the population.
- `crossover_rate`: The probability of performing crossover on a pair of parents.
- `mutation_rate`: The probability of mutating an individual.
- `grid_size`: The size of the grid for the Game of Life simulation.

These parameters can be adjusted in the `main.py` file to change the behavior of the genetic algorithm and the Game of Life simulation.

## Dependencies

The script requires the following Python libraries:

- `numpy`
- `random`

These can be installed using pip:

```bash
pip install numpy
```

## License

This project is licensed under the MIT License.
