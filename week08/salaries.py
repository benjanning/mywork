# A programme that ouputs random salaries, adds 5000 to each salary, adds %5
# Author: Ben Janning

from random import seed
import numpy as np

# setting absolute in to variables

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

# making random salary print the same result each time
np.random.seed(1)

print (salaries)

# adding 5000 to each salary
salariesPlus = salaries + 5000

print (salariesPlus)

#adding 5% to the salaries
salariesMult = salaries * 1.05

print (salariesMult)



