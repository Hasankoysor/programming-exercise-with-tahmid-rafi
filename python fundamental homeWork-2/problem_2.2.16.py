# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 19:21:07 2022

@author: MD KOYSOR HASAN
"""

person1 = int(input())
person2 = int(input())
person3 = int(input())
person4 = int(input())
person5 = int(input())
person6 = int(input())


more_than_thirty = 0



if person1 >= 30:
    more_than_thirty += 1 # more_than_thirty = more_than_thirty + 1
if person2 >= 30:
    more_than_thirty += 1
if person3 >= 30:
    more_than_thirty += 1
if person4 >= 30:
    more_than_thirty += 1
if person5 >= 30:
    more_than_thirty += 1
if person6 >= 30:
    more_than_thirty += 1
print("the number more than 30 age are: ",more_than_thirty)