# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:41:41 2022

@author: MD KOYSOR HASAN
python fundamantal hw-2
"""

office_open = bool(int(input()))
special_program = bool(int(input()))

weak_up = office_open or special_program

if weak_up:
    print("You need to weak up early! ")
if not weak_up:
    print("Sleep! you do not need to work today...")
