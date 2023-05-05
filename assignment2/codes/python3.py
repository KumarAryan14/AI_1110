import itertools

# create a list of all possible combinations of 4 digits without repeats using permutation function from itertools.
combinations = list(itertools.permutations(range(10),4))

# calculate the total number of combinations using len function to calculate length of list(combination).
total_combinations = len(combinations)

# count the number of combinations that open the suitcase letting correct sequence be (1, 2, 3, 4)
correct_combinations = sum([1 for c in combinations if c == (1, 2, 3, 4)])

# calculating the probability of guessing the right sequence
probability = correct_combinations / total_combinations

print('The probability of guessing the right sequence is :',probability)

