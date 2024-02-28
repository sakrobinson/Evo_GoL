import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import main

# Convert the ruleset to the expected format
ruleset = {'survive': [i for i in range(9) if [0, 0, 0, 1, 0, 0, 0, 1, 1][i] == 1], 'birth': [3]}

# Create an initial state
initial_state = np.random.randint(2, size=(10, 10))

# Simulate the Game of Life with the given ruleset and initial state for a certain number of steps
final_state, states = main.simulate_game_of_life(initial_state, ruleset, steps=10)

# Print the final state
print(final_state)

# Create a figure and a plot
fig, ax = plt.subplots()

# Function to update the plot
def update(i):
    ax.clear()
    ax.imshow(states[i], cmap='binary')

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=len(states))

# Display the animation
plt.show()