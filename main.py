import matplotlib.pyplot as plt
import numpy as np
import random
from time import sleep
x = []
counter = 0
minNo = 0
arr = []

a = int(input())
for i in range(1,a + 1):
    x.append(i)
    arr.append(i)

plt.ylabel("y")
plt.xlabel("x")
plt.title("Sorting Visualisation")
random.shuffle(arr)
print(arr)
def Sort():
    global counter
    global minNo
    
    if counter < a:
        if arr[counter] != minNo + 1 and arr[counter] != minNo:

            minNo = min(arr[counter:len(arr)])
            tempNo = arr[counter]
            
            arr.remove(arr[arr.index(minNo)])
            arr[counter] = minNo
            arr.append(tempNo)
        counter += 1




plt.ion()
while counter  < a:
    plt.bar(x,arr)
    plt.draw()
    plt.pause(0.5)
    plt.bar(x,arr,color = "red")
    plt.draw()
    Sort()
    print(arr)
    if counter != a:
        plt.pause(0.1)
        plt.clf()






sleep(5)


    


    
