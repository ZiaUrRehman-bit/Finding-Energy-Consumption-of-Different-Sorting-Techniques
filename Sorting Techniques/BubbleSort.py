import time
import psutil, os
from memory_profiler import profile

# generating a random number
import random

# @profile          # in order to see the memory utilization
def bubbleSort():
    n = 100
    list = []

    for i in range(0, n):   # for i in range(n,0,-1):  for reverse sorted list of number
        list.append((random.randint(1,1000)))
        # list.append(i)

    # print(f"Before Sorting: {list}")

    start = time.time()
    for i in range(0,n-1):
        
        for j in range(0,n-i-1):
            
            if list[j] > list[j+1]:
                
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    cpu1 = psutil.cpu_percent(interval=1)  

    end = time.time()

    cpu2 = psutil.cpu_percent(interval=1)  
    # print(f"After Sorting: {list}")

    print(f"Time Take: {end-start} seconds")
    print(f"CPU utilization: {cpu1}, {cpu2}")

bubbleSort()
