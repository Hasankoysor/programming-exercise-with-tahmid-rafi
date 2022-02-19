# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 16:33:19 2022

@author: MD KOYSOR HASAN
"""

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
num6 = int(input())
millionaire = 0



if num1 >= 1000000:
    millionaire += 1 # millionare = millionare + 1
if num2 >= 1000000:
    millionaire += 1
if num3 >= 1000000:
    millionaire += 1
if num4 >= 1000000:
    millionaire += 1
if num5 >= 1000000:
    millionaire += 1
if num6 >= 1000000:
    millionaire += 1
print("Number of millionaries: ",millionaire)