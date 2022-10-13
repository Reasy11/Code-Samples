
import numpy as np
import random
import copy


#Define function to generate random permutations
def rand_permutation_generator(a):
    candidates = list()
    while len(candidates) < 1000:              #The len function determines the length of a given element.
        random.shuffle(a)                      #random.shuffle works as a randomized in-place sorting method. It swaps A[1] with random A[N] then repeats process for A[2] through A[N].
        if a not in candidates:
            candidates.append(copy.deepcopy(a))
    return candidates

#Define function to determine number of hires per permutation
def rand_hire_assitant(Candidates):
    hires = list()
    for i in range(len(Candidates)):            #The range function determines the range of a given element. i.e. the range of 20 is 1 - 20.
        best = 0
        count = 0
        for j in range(len(Candidates[i])):
            if (Candidates[i, j] > best):
                best = Candidates[i, j]
                count += 1
        hires.append(count)                     #The .append function append an element into a list.
    hires = np.array(hires)                     #The np.array function converts a list into an array.
    return hires

#Generate 1000 random permutations for 8!
a = list(range(1,9))
Candidates = rand_permutation_generator(a)

#Determine number of hires for 1000 8! permuations and calculate total number of hires
Candidates = np.array(Candidates)
Hires = rand_hire_assitant(Candidates)
mean_hires_8 = np.sum(Hires)/1000               #The np.sum function determines the sum of an arrays elements. i.e. 1 + 2 + 3 = 6

#generate 1000 random permutations for 20!
a = list(range(1, 21))
Candidates = rand_permutation_generator(a)

#Determine number of hires for 1000 20! permuations and calculate total number of hires
Candidates = np.array(Candidates)
Hires = rand_hire_assitant(Candidates)
mean_hires_20 = np.sum(Hires)/1000

#Comparisions for 8! permutations
exhaustive_expectation = 2.717857142857143

if mean_hires_8 > exhaustive_expectation:
    print("Randomized mean of 1000 8! permutations =", mean_hires_8, "> exhaustive mean =", exhaustive_expectation)
else:
    print("Randomized mean of 1000 8! permutations =", mean_hires_8, "< exhaustive mean =", exhaustive_expectation)

#Comparisons for 20! permutations
lecture_expectation = 0

for i in range(1, 21):
    lecture_expectation += (1/i)

if mean_hires_20 > lecture_expectation:
    print("Randomized mean of 1000 20! permutations =", mean_hires_20, "> theoretical expectation =", lecture_expectation)
else:
    print("Randomized mean of 1000 20! permutations =", mean_hires_20, "< theoretical expectation =", lecture_expectation)

# The mean number of hires varies slightly between rand_hire_assistant runs due to the random permutations used in each run.
# However, even with this slight variation the mean hires of 1000 8! (around 2.65 - 2.75) permutations is always close to the exhaustive mean (2.717857142857143) we calculated in homework 1.
# The same can be said for the mean hires of 1000 20! (around 3.55 - 3.7) except we do not have an exhaustive mean to compare it to. Instead we compare it to the theoretical expectation (3.597739657143682). Which we calculate with the formula (1/1 + 1/2 + 1/3... + 1/n).