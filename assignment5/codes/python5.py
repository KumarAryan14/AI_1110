import numpy as np

# n denotes number of items
n = 10

# p denotes probability of defective item
p = 0.05

trials = 1000000

# simulate binomial distribution
simulations = np.random.binomial(n,p,trials)

# calulatiing probability of X>= 12
prob = np.sum(simulations <=1)/trials

print('Probability :',prob)









