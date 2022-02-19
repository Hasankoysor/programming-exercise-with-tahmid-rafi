# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = int(input())
b = int(input())
c = int(input())

minimum = a
middle = b
maximum = c

if a < b and a < c:
    minimum = a
if a > b and a > c:
    maximum = a
if a > b and a < c:
    middle = a
if b > a and b > c:
    maximum = b
if b < a and b < c:
    minimum = b
if b > a and b < c:
    middle = b
if c > a and c > b:
    maximum = c
if c < a and c < b:
    minimum = c
if c > a and c < b:
    middle = c
print(minimum,middle,maximum)