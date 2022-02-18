# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 02:21:59 2022

@author: MD KOYSOR HASAN
"""

x = int(input())
y = int(input())

need_food = (x*3)*7

if y >= need_food:
    print("Enough food for this week!")
    
if y < need_food:
    print("Not enough food for this week........")