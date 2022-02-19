# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 02:11:28 2022

@author: MD KOYSOR HASAN
"""

import math

number = int(input())

sqr_root = math.sqrt(number)

if sqr_root * sqr_root == number:
    print("The number is squre number")

if sqr_root * sqr_root != number:
    print("The number is not squre number")

