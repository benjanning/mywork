# A programme that writes a histogram of salaries
# Author: Ben Janning

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

# making the random numbers the same each time, so it's easier to debug

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

plt.hist(salaries)
plt.show ()