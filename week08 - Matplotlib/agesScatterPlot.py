# a program that makes a list called ages that has, the same number random
# values as salaries. making a scatter plot of the data.
# Author: Ben Janning

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

# making the random numbers the same each time so it's easier to debug.

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint (low = 21, high = 65, size = numberOfEntries)

plt.scatter (ages, salaries)
#plt.show ()

#Add a line to this plot that shows y= x2 in a different colour
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color = "r", label = "x squared")
plt.title("random plot")
plt.xlabel("salaries")
plt.ylabel("age")
plt.legend()
plt. show()


