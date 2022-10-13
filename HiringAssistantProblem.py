from itertools import permutations
import math
import numpy as np
from numpy import log as ln

#Generate all 8! Permutations of candidates
A = list(permutations(range(1, 9)))
Candidates = np.array(A)

#Find number of hires per permutation
hires = list()

for i in range(len(Candidates)):
    best = 0
    count = 0
    for j in range(len(Candidates[i])):
        if (Candidates[i,j] > best):
            best = Candidates[i, j]
            count += 1
    hires.append(count)
hires = np.array(hires)

#Calculations
#mean hires
mean_hires = (np.sum(hires)/40320)

#Theoretical expectation
expectation = (1/math.factorial(8))*(np.sum(hires))

#Lecture expecation
lecture_expectation = 0

for i in range(1,9):
    lecture_expectation += (1/i)

#Variance
hires_squared = np.zeros(len(hires))

for i in range(len(hires)):
    hires_squared[i] = hires[i]**2
variance = (1/math.factorial(8))*(np.sum(hires_squared))-expectation**2

#Comparisons
print("Theoretical expectation (EH) = ", expectation)
print("Lecture expectation = ", lecture_expectation)
print("Theoretical variance (Var(H)) = ", variance)
print("Value of ln(8) = ", ln(8))
print("Theoretical expectation ~= Lecture Expectation and > ln(8)")
print(mean_hires)

