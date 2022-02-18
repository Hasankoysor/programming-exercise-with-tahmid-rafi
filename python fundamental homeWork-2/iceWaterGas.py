# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 01:12:33 2022

@author: MD KOYSOR HASAN
"""

temp = int(input())

if temp < 0:
    print("Ice(solid)")
if temp > 0 and temp <= 100:
    print("Water(liquid)")
if temp > 100:
    print("Steam(gas)")