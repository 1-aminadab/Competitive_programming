# print('Amanuel Tadesse')
#
# name = "team company";
# age = 25;
#
# print(name)
# print(age)
#
# full_name = 'amanuel tadess'
# print(full_name)
#
# width, height = 400, 500;
#
# print(width)
# print(height)
#
# # your_name = input('please inter your name')
# # print(your_name)
#
# num1 =input('enter first number: ')
# num2 =input('enter second number: ')
# print(int(num1)+int(num2))
#
# food_amount = float(input('enter food_amount:'))
# tip_percent = float(input('inter tip percentage:'))
# tip = food_amount * tip_percent/100;
#
# total_amount = food_amount + tip;
# print('_______________________________')
# print(f'food amount:  ${food_amount}')
# print(f'tip amount:   ${tip}')
# print(f'total amount: ${total_amount}')
# print('--------------------------------')
#
# weather = 'rain'
#
# if weather == 'rain':
#     print('grab umbrella')
# else:
#     print('wear sun-glass')
#

# score = float(input('enter your score: '))
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# elif score < 60:
#     print('F')
# else:
#     print('you enter the wrong score... try again')


# class Solution(object):
#     def fizzBuzz(self, n):
#         i = []
#
#         for x in range(1, n + 1):
#             if x % 3 == 0 and x % 5 == 0:
#                 i.append("FizzBuzz")
#             elif x % 3 == 0:
#                 i.append("Fizz")
#             elif x % 5 == 0:
#                 i.append("Buzz")
#             else:
#                 i.append(str(x))
#
#         print(i)
#
#
# p1 = Solution()
# p1.fizzBuzz(3)


# class Domino:
#     def __init__(self,width,height):
#         rectangle = width * height
#         domino = 2
#         output  = rectangle/domino
#         print(int(output))
#
#
# result = Domino(1,5)

# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#


def countSwaps(a):
    # Write your code here
    n = len(a)
    swap = 0
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap += 1
    print(f'Array is sorted in {swap} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[len(a) - 1]}')

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
