#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    
    result = []
    # to get the maximum range
    largestValue =0
    for i in range(len(arr)):
        if largestValue < arr[i]:
            largestValue = arr[i] 
    print(largestValue)        
    for i in range(100):
        result.append(int(0)) 
           
    for j in range(len(arr)):
        incrementIndex = arr[j]
        result[incrementIndex] += 1
    
    return result 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    result = countingSort(arr)
    
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
