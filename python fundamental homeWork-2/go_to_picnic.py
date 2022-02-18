# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 19:00:48 2022

@author: MD KOYSOR HASAN
"""

a = int(input())
b = int(input())
c = int(input())
number_of_frds = 6

go_picnic = a*number_of_frds >= b+(number_of_frds*c )

if go_picnic:
    print("We can go to picnic....")
    
if not go_picnic:
    print("We can't go to picnic today!")