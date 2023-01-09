# Description: This script plots the entanglement and product states probabilities 
# as a function of the angle theta for the 2-propeller system.
# Author: Nada Ali
# Date: 2023-02-01

# --------------------------------------------------------------- #

import numpy as np
import matplotlib.pyplot as plt

# Create an array of theta values from 0 to 2*pi
theta = np.linspace(0, 360, 100)
theta = theta * np.pi / 180

# Evaluate the first function for each value of theta
y1 = 1/6 * (3 + 2 * np.sin(2*theta) + np.sin(4*theta))

# Evaluate the second function for each value of theta
y2 = -(1/12) * np.cos(2 * theta) + 1/12 * (7 + np.sqrt(2) * np.sqrt((2 + 8 * np.cos(theta)**2 + 5 * np.cos(theta)**4 + np.cos(theta)**6 - np.cos(theta) * np.sqrt(32 + 100 * np.cos(theta)**2 + 68 * np.cos(theta)**4 + 45 * np.cos(theta)**6 + 10 * np.cos(theta)**8 + np.cos(theta)**10)) * np.sin(theta)**2) + np.sqrt(2) * np.sqrt((2 + np.cos(theta) * (8 * np.cos(theta) + 5 * np.cos(theta)**3 + np.cos(theta)**5 + np.sqrt(32 + 100 * np.cos(theta)**2 + 68 * np.cos(theta)**4 + 45 * np.cos(theta)**6 + 10 * np.cos(theta)**8 + np.cos(theta)**10))) * np.sin(theta)**2))

# Limit probbility to only positive values
y1[y1 < 0] = 0
y2[y2 < 0] = 0
# Create an ordinary plot
plt.plot( theta, y1, label='Entanglement probability')
plt.plot( theta, y2, label='Product probability')

# Set the x-axis label
plt.xlabel(r'$\theta$')

# Set the y-axis label
plt.ylabel('Probability')

# Set the plot title
plt.title('Entanglement and product probabilities')

# Add a legend
plt.legend()

# Save the plot as a pdf file
plt.savefig('fig.pdf')


# Show the plot
plt.show()
