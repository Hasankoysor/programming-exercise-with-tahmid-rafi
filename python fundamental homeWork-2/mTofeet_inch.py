# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:18:40 2022

@author: MD KOYSOR HASAN
"""

print("This program will convert a height given meters to a height given in feet and inches.")
meters = float(input("Enter height in meters:"))
meters_in_ft = meters // .3048
inches = meters / .3048 % 1 * 12
print("The height is", meters_in_ft,"feet and",inches, "inches")