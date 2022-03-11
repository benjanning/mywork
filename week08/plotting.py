# a program that plots the function y = x2.
# Author: Ben Janning

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array (range(1, 101))
ypoints = xpoints * xpoints #multiplying entry by itself

plt.plot (xpoints, ypoints)
plt.show()
