import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import main  # Import the GA module you've created

def animate_ruleset(ruleset, steps=100, interval=200):
    """
    Create an animation for a given ruleset.
    :param ruleset: The ruleset to simulate and animate.
    :param steps: Number of simulation steps to animate.
    :param interval: Time interval between frames in milliseconds.
    """
    fig, ax = plt.subplots()
    initial_state = np.random.randint(2, size=(10, 10))
    states = [initial_state]

    def init():
        im.set_data(states[0])
        return [im]

    def update(frame):
        if frame == 0:
            states.append(main.step_game_of_life(states[-1], ruleset))
        else:
            states.append(main.step_game_of_life(states[-1], {'survive': ruleset['survive'], 'birth': ruleset['birth']}))
        im.set_data(states[-1])
        return [im]

    im = ax.imshow(states[0], animated=True)
    ani = FuncAnimation(fig, update, frames=range(steps), init_func=init, blit=True, interval=interval)
    plt.close()  # Prevents the initial frame from showing up, only display animation
    return ani

def visualize_top_n_rulesets(n=5):
    """
    Find the top n rulesets from the genetic algorithm and visualize them.
    :param n: Number of top rulesets to visualize.
    """
    # Assuming the genetic algorithm stores the top n rulesets in a specific way
    # You need to adjust this part based on how you retrieve the top n rulesets
    # For demonstration, let's simulate finding top n rulesets
    top_rulesets = [main.genetic_algorithm() for _ in range(n)]  # You'll replace this with actual top n retrieval

    for i, (ruleset, score) in enumerate(top_rulesets):
        ani = animate_ruleset(ruleset)
        ani.save(f"ruleset_{i+1}_animation.gif", writer='imagemagick')
        print(f"Ruleset {i+1} animation saved as ruleset_{i+1}_animation.gif")

if __name__ == "__main__":
    visualize_top_n_rulesets()
