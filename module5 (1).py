'''
John Detloff
Module 5
Sorting and Searching Algorithms
'''

import time
import random
import matplotlib.pyplot as plt

def bubbleSort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

def QSpartition(lst, low, high):
    pivot = lst[low]
    i = low + 1

    while True:
        while i <= high and lst[high] >= pivot:
            high = high - 1

        while i <= high and lst[i] <= pivot:
            i = i+1

        if i <= high:
            lst[i], lst[high] = lst[high], lst[i]
        else:
            break

    lst[low], lst[high] =  lst[high], lst[low]

    return high

def quickSort(lst, low, high):
    if low >= high:
        return

    p = QSpartition(lst, low, high)
    quickSort(lst, low, p-1)
    quickSort(lst, p+1, high)

def shellSort(lst):
    y = len(lst)
    x = y//2
    while x > 0:
        for i in range(x, y):
            temp = lst[i]
            j = i
            while j >= x and lst[j-x] > temp:
                lst[j] = lst[j-x]
                j -= x

            lst[j] = temp
        x = x//2
        

def sort(x):
    
    mylist = []
    for i in range(0, x):
        y = random.randint(1 ,x)
        mylist.append(y)

    start_time = time.time()
    bubbleSort(mylist)
    #quickSort(mylist, 0, len(mylist)-1)
    #shellSort(mylist)
    
    timer = time.time() - start_time
    print(x, "\t \t", format(timer, '.2f'), " sec")
    return timer

def main(): 
    times = []
    print("Data Set \t Time")
    times.append(sort(10000))
    times.append(sort(30000))
    times.append(sort(50000))
    times.append(sort(70000))
    times.append(sort(90000))

    ranges=[10000, 30000, 50000, 70000, 90000]

    plt.plot(ranges, times)
    plt.title('Time to Sort vs. Size of Dataset')
    plt.xlabel('Size of Dataset')
    plt.ylabel('Time To Sort (seconds)')
    plt.show()

main()




