# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 17:18:06 2022

@author: MD KOYSOR HASAN
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input()) # where is the problem on this code?

first = a 
second = b
third = c 
fourth = d

if a < b and a < c and a < d:
    first = a
if a > b and a < c and a < d:
    second = a 
if a > b and a > c and a < d:
    third = a 
if a > b and a > c and a > d:
    fourth = a
if b < a and b < c and b < d:
    first = b
if b > a and b < c and b < d:
    second = b
if b > a and b > c and b < d:
    third = b
if b > a and b > c and b > d:
    fourth = b
if c < a and c < b and c < d:
    first = c
if c > a and c < b and c < d:
    second = c
if c > a and c > b and c < d:
    third = c
if c > a and c > b and c > d:
    fourth = c
if d < a and d < b and d < c:
    first = d
if d > a and d < b and d < c:
    second = d
if d > a and d > b and d < c:
    third = d
if d > a and d > b and d > c:
    fourth = d
print(first,second,third,fourth)