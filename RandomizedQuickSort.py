import random

#Define comparisons counter
class counters:
    def __init__(self):
        self.comparisonsCount = 0
    def incrementComparisonsCount(self):
        self.comparisonsCount += 1
    def getComparisonsCount(self):
        return self.comparisonsCount

#Define Partition
def Partition(array, low, high):
    pivot = high                                                                    #set the pivot
    i = low - 1
    for j in range(low, high):                                                      #Process every element other than the pivot
        test.incrementComparisonsCount()                                            #increase comparisons counter
        if array[j] <= array[pivot]:                                                #Check to see if this element belongs on the low side of the array
            i = i + 1                                                               #Create a new slot on the low side
            array[i], array[j] = array[j], array[i]                                 #Add this element to new slot on the low side
    array[i+1], array[high] = array[high], array[i+1]                               #place pivot just to the right of the low side
    return i + 1                                                                    #return the new index of the pivot

#Define RandomizedPartition
def RandomizedPartition(array, low, high):
    randPivot = random.randrange(low, high)                                         #the random.randrange function chooses a random item from a specific range. In this case between p and q.
    array[high], array[randPivot] = array[randPivot], array[high]                   #Swap A[high] with with the random pivot
    return Partition(array, low, high)

#Define RandomizedQuickSort
def RandomizedQuickSort(array, low, high):
    if low < high:
        pivot = RandomizedPartition(array, low, high)                               #Create a random pivot within the array
        RandomizedQuickSort(array, low, pivot-1)                                    #Sort the left half of the array
        RandomizedQuickSort(array, pivot+1, high)                                   #Sort the right half of the array

#Call RandomizedQuickSort
test = counters()
array = [5, 8, 17, 3, 14, 20, 18, 19, 10, 9, 7, 6, 15, 11, 4, 1, 16, 2, 13, 12]
RandomizedQuickSort(array, 0, len(array)-1)

#upperbound calculation
n = 20
sum = 0
for i in range(0, n-1):
    for k in range(0, n):                                                           #calculate the value of k for each iteration of n (n = 20)
        if k > 0:
            sum += (2.0/k)
print("Total number of Comparisons:", test.getComparisonsCount())
print("Upperbound:", sum)

#The upper bound given in the textbook is defined as the summation of i = 1 through n -1 and the summation of k = 1 through n for 2/k.
#When we compute this bound for n = 20 (because the array has 20 elements) we get an upperbound of 134.81
#The total number of comparisons varies between each run of the program due the randomization of the pivot.
#But the total number of comparisons is typically between 60 and 80 comparisons and it is always less than the upperbound of 134.81.
#So, we can say that the number of comparisons is in agreement with the bound.