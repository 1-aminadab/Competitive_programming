#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(n, arr):
    # Write your code here
    
    lastIndex = n-1
    lastNum = arr[lastIndex]
    
    for i in range(1, len(arr)):

        if arr[lastIndex-i] > lastNum:

            arr[lastIndex-i+1] = arr[lastIndex-i]
        else:
            arr[lastIndex-i+1] = lastNum

        print(*arr, sep=" ")
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
