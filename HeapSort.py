
import random
import copy


#Define heapsort and buildmaxheap counters
class counters:
    def __init__(self):
        self.heapsortCount = 0
        self.buildmaxheapCount = 0
    def incrementHeapSortCount(self):
        self.heapsortCount += 1
    def incrementBuildMaxHeapCount(self):
        self.buildmaxheapCount += 1
    def getHeapSortCount(self):
        return self.heapsortCount
    def getBuildMaxHeapCount(self):
        return self.buildmaxheapCount

#Define function to generate random permutations
def rand_permutation_generator(a):
    permutations = list()
    while len(permutations) < 2000:            #The len function determines the length of a given element.
        random.shuffle(a)                      #random.shuffle works as a randomized in-place sorting method. It swaps A[1] with random A[N] then repeats process for A[2] through A[N].
        if a not in permutations:
            permutations.append(copy.deepcopy(a))
    return permutations

#Define function heapsort
def heapsort(a,test):
    n = len(a)
    build_max_heap(a)
    for i in range(n-1, 0, -1):                #The range function determines the range of a given element. i.e. the range of 20 is 1 - 20.
        a[0], a[i] = a[i], a[0]                #Swap A[1] with A[i]
        test.incrementHeapSortCount()          #Increases the heapsort count by one
        n = n - 1
        max_heapify(a, i, 0, test)


#Define function to build max heaps
def build_max_heap(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, - 1):        #Start building a max heap at the last parent location.
        max_heapify(a, n, i, test)


#Define function Max_heapify
def max_heapify(a, n, i, test):
    left = 2 * i + 1                            #Define left child
    right = 2 * i + 2                           #Define right child
    if left < n and a[left] > a[i]:             #Compare left child to root
        largest = left
    else:
        largest = i
    if right < n and a[right] > a[largest]:     #Compare Right child to root
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]     #Swap the root if necessary
        test.incrementHeapSortCount()
        test.incrementBuildMaxHeapCount()       #Increases the buildmaxheap count by one.
        max_heapify(a, n, largest, test)

#Define function to heapsort 2000 random permutations of 20!
def heapsort_bunch(permutations, test):
    while permutations:
        heapsort(permutations.pop(), test)      #The .pop method removes an element from a list or array.

#generate 2000 random permutations for 20!
array = list(range(1, 21))
permutations = rand_permutation_generator(array)

#Run heapsort on 2000 permutations of 20!
test = counters()
#heapsort_bunch(permutations, test)
heapsort(array, test)
print(array)

#Calculate number of swaps
mean_swaps_BMX = test.getBuildMaxHeapCount()
mean_swaps_HP = test.getHeapSortCount()
print("average buildmaxheap swaps: ", mean_swaps_BMX)
print("average heapsort swaps: ", mean_swaps_HP)
