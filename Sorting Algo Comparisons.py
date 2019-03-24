#  File: sorting.py
#  Description: Compares the efficiency of various sorting algorithms
#  Student's Name: Johnathan Tran
#  Student's UT EID: jht697
#  Course Name: CS 313E
#  Unique Number: 51470
#
#  Date Created: 11/29/2017
#  Date Last Modified: 12/1/2017

import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

# generates a random list of n ints
def randomGen(n):

    randomList = []

    for num in range(n):
        randomList.append(num)

    random.shuffle(randomList)

    return randomList

# generates a sorted list of n ints
def sortedGen(n):

    sortedList = []

    for num in range(n):
        sortedList.append(num)

    return sortedList

# generates a reverse sorted list of n ints
def reverseGen(n):

    alist = []
    reverseList = []

    for num in range(n):
        alist.append(num)

    for num in range(len(alist)):

        a = alist.pop()
        reverseList.append(a)

    return reverseList

# generates a list of n ints that is almost sorted
def almostSortedGen(n):

    sortedList = []

    for num in range(n):
        sortedList.append(num)

    swaps = len(sortedList) // 10

    for i in range(swaps):

        ranIndex1 = random.randint(0,len(sortedList)-1)
        ranIndex2 = ranIndex1

        while ranIndex2 == ranIndex1:
            ranIndex2 = random.randint(0,len(sortedList)-1)

        num1 = sortedList[ranIndex1]
        num2 = sortedList[ranIndex2]

        sortedList[ranIndex1], sortedList[ranIndex2] = sortedList[ranIndex2], sortedList[ranIndex1]

    return sortedList

# finds the average time of any given sort
def avgSortTime(alist,sortType):

    avgTimes = []
    times = []

    for i in range(5):

        # sorts the list using given sort type
        if sortType == 'bubble':
            startTime = time.clock()
            bubbleSort(alist)

        elif sortType == 'insertion':
            startTime = time.clock()
            insertionSort(alist)

        elif sortType == 'merge':
            startTime = time.clock()
            mergeSort(alist)

        elif sortType == 'quick':
            startTime = time.clock()
            quickSort(alist)

        # stops the timer and calculates time elapsed
        endTime = time.clock()
        elapsedTime = endTime - startTime
        times.append(elapsedTime)

    i = 0
    while i in range(len(times)):

        sums = 0
        sums += times[i]
        avgSortTime = float(sums) / 5.0

        i += 1

    return "{:.6f}".format(avgSortTime)


def printTable(inputType,bubbleTimes,insertionTimes,mergeTimes,quickTimes):

    # prints the table for given input type
    print("Input type = " + str(inputType))
    print("                   avg time   avg time   avg time")
    print("   Sort function    (n=10)    (n=100)    (n=1000)")
    print("-------------------------------------------------")

    print("      bubbleSort   " + str(bubbleTimes[0]) + "   " + str(bubbleTimes[1]) + "   " + str(bubbleTimes[2]))
    print("   insertionSort   " + str(insertionTimes[0]) + "   " + str(insertionTimes[1]) + "   " + str(insertionTimes[2]))
    print("       mergeSort   " + str(mergeTimes[0]) + "   " + str(mergeTimes[1]) + "   " + str(mergeTimes[2]))
    print("       quickSort   " + str(quickTimes[0]) + "   " + str(quickTimes[1]) + "   " + str(quickTimes[2]))
    print()
    print()


def main():

    trials = [10,100,1000]

    # retrieves times for random order list
    bubbleTimes = []
    insertionTimes = []
    mergeTimes = []
    quickTimes = []

    for i in range(0,len(trials)):

        ranList = randomGen(trials[i])

        # finds the average time of a bubble sort for different list lengths
        avgBubble = avgSortTime(ranList,'bubble')
        bubbleTimes.append(avgBubble)

        # finds the finds the average time of an insertion sort for different list lengths
        avgInsertion = avgSortTime(ranList,'insertion')
        insertionTimes.append(avgInsertion)

        # finds the finds the average time of a merge sort for different list lengths
        avgMerge = avgSortTime(ranList,'merge')
        mergeTimes.append(avgMerge)

        # finds the finds the average time of a quick sort for different list lengths
        avgQuick = avgSortTime(ranList,'quick')
        quickTimes.append(avgQuick)


    # retrieves times for sorted list
    bubbleTimes2 = []
    insertionTimes2 = []
    mergeTimes2 = []
    quickTimes2 = []

    for i in range(0,len(trials)):

        sortList = sortedGen(trials[i])

        # finds the average time of a bubble sort for different list lengths
        avgBubble = avgSortTime(sortList,'bubble')
        bubbleTimes2.append(avgBubble)

        # finds the finds the average time of an insertion sort for different list lengths
        avgInsertion = avgSortTime(sortList,'insertion')
        insertionTimes2.append(avgInsertion)

        # finds the finds the average time of a merge sort for different list lengths
        avgMerge = avgSortTime(sortList,'merge')
        mergeTimes2.append(avgMerge)

        # finds the finds the average time of a quick sort for different list lengths
        avgQuick = avgSortTime(sortList,'quick')
        quickTimes2.append(avgQuick)


    # retrieves times for reverse sorted list
    bubbleTimes3 = []
    insertionTimes3 = []
    mergeTimes3 = []
    quickTimes3 = []

    for i in range(0,len(trials)):

        revList = reverseGen(trials[i])

        # finds the average time of a bubble sort for different list lengths
        avgBubble = avgSortTime(revList,'bubble')
        bubbleTimes3.append(avgBubble)

        # finds the finds the average time of an insertion sort for different list lengths
        avgInsertion = avgSortTime(revList,'insertion')
        insertionTimes3.append(avgInsertion)

        # finds the finds the average time of a merge sort for different list lengths
        avgMerge = avgSortTime(revList,'merge')
        mergeTimes3.append(avgMerge)

        # finds the finds the average time of a quick sort for different list lengths
        avgQuick = avgSortTime(revList,'quick')
        quickTimes3.append(avgQuick)


    # retrieves times for almost sorted list
    bubbleTimes4 = []
    insertionTimes4 = []
    mergeTimes4 = []
    quickTimes4 = []

    for i in range(0,len(trials)):

        almostSortList = almostSortedGen(trials[i])

        # finds the average time of a bubble sort for different list lengths
        avgBubble = avgSortTime(almostSortList,'bubble')
        bubbleTimes4.append(avgBubble)

        # finds the finds the average time of an insertion sort for different list lengths
        avgInsertion = avgSortTime(almostSortList,'insertion')
        insertionTimes4.append(avgInsertion)

        # finds the finds the average time of a merge sort for different list lengths
        avgMerge = avgSortTime(almostSortList,'merge')
        mergeTimes4.append(avgMerge)

        # finds the finds the average time of a quick sort for different list lengths
        avgQuick = avgSortTime(almostSortList,'quick')
        quickTimes4.append(avgQuick)


    # print the table for random list
    printTable("Random",bubbleTimes,insertionTimes,mergeTimes,quickTimes)

    # print the table for sorted list
    printTable("Sorted",bubbleTimes2,insertionTimes2,mergeTimes2,quickTimes2)

    # print the table for reverse sorted list
    printTable("Reverse",bubbleTimes3,insertionTimes3,mergeTimes3,quickTimes3)

    # print the table for almost sorted list
    printTable("Almost sorted",bubbleTimes4,insertionTimes4,mergeTimes4,quickTimes4)

main()
