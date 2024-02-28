import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import main  # Import the GA module you've created

def animate_ruleset(individual, steps=100):
    """
    Create an animation for a given ruleset.
    :param ruleset: The ruleset to simulate and animate.
    :param steps: Number of simulation steps to animate.
    """
    # Create an initial state
    (ruleset, initial_state), _ = individual
   
    #ruleset = list(ruleset)  # Flatten the numpy array and convert to list
    ruleset_dict = {'survive': [i for i in range(9) if ruleset[i] == 1], 'birth': [3]}
    # Simulate the Game of Life with the given ruleset and initial state for a certain number of steps
    final_state, states = main.simulate_game_of_life(initial_state, ruleset_dict, steps)

    # Create a figure and a plot
    fig, ax = plt.subplots()

    # Function to update the plot
    def update(i):
        ax.clear()
        ax.imshow(states[i], cmap='binary')

    # Create an animation
    ani = FuncAnimation(fig, update, frames=len(states), blit=True)

    plt.close()  # Prevents the initial frame from showing up, only display animation
    return ani

def visualize_top_n_rulesets(n=5, top_rulesets=[]):
    """
    Find the top n rulesets from the genetic algorithm and visualize them.
    :param n: Number of top rulesets to visualize.
    :param top_rulesets: The best performing rulesets in GoL from run.py
    """

    for i, individual in enumerate(top_rulesets):
        ani = animate_ruleset(individual)
        ani.save(f"ruleset_{i+1}_animation.gif", writer='imagemagick')
        #print(f"Ruleset {i+1} animation saved as ruleset_{i+1}_animation.gif")

if __name__ == "__main__":
    visualize_top_n_rulesets()
