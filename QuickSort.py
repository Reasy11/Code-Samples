
from numpy import log as ln

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
        if array[j] <= array[pivot]:                                                #Check to see if this element belongs on the low side of the array
            i = i + 1                                                               #Create a new slot on the low side
            array[i], array[j] = array[j], array[i]                                 #Add this element to new slot on the low side
            test.incrementComparisonsCount()                                        #increase comparisons counter
    array[i+1], array[high] = array[high], array[i+1]                               #place pivot just to the right of the low side
    return i + 1                                                                    #return the new index of the pivot

#Define QuickSort
def QuickSort(array, low, high):
    if low < high:
        pivot = Partition(array, low, high)                               #Create a random pivot within the array
        QuickSort(array, low, pivot-1)                                    #Sort the left half of the array
        QuickSort(array, pivot+1, high)                                   #Sort the right half of the array

#Call QuickSort
test = counters()
array = [9, 1, 20, 8, 14, 3, 10, 5, 17, 15, 12]
QuickSort(array, 0, len(array)-1)
print(array)
print(test.getComparisonsCount())

upperbound = (20*ln(20))
print(upperbound)