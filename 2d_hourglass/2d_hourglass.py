import math
import os
import random
import re
import sys


R=6
C=6
def hourglassSum(arr):
    
    max_sum = -50000
    
        
    for i in range(0,R-2):
        for j in range(0,C-2):
            Sum = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2]) + (arr[i + 1][j + 1]) +(arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])
            if (Sum > max_sum):
                max_sum = Sum
                
            else:
                continue 

                
    return max_sum
    
def rotateLeft(d, arr):
    # Write your code here
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr

if __name__ == '__main__':
    arr = [[1, 2, 3, 0, 0],
       [0, 0, 0, 0, 0],
       [2, 1, 4, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 1, 0, 1, 0]]

    res =hourglassSum(arr)
    print(f"Maximum sum of hour glass = {res}")