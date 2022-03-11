# Demonstrate making a pie plot of the unique occurences of values in an array.
# Author: Ben Janning

import numpy as np
import matplotlib.pyplot as plt

# make the array of occurences
possibleCounties = ("Mayo, Galway, DirtyDublin, Kerry, Donegal")

# pick 100 randomly from counties with the frequency set in p
counties = np.random.choice(
        possibleCounties, 
        p = [0.1, 0.3, 0.2, 0.12, 0.28 ],
        size = (100)
)

# getting the number of occurences in each County
# This returns a Tuple of the unique value and how many times they appear
unique, counts = np.unique(counties, return_counts=True)

# putting this in a pie chart
plt.pie(counts, labels = unique)

plt.show()



