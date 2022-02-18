# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 01:52:20 2022

@author: MD KOYSOR HASAN
"""

total_numbers_of_friends = 5
total_sit = int(input())
current_number_of_passenger = int(input())

will_get_sit = current_number_of_passenger + total_numbers_of_friends <= total_sit
if will_get_sit:
    print("All of us could ride bus")
if not will_get_sit:
    print("wait for next bus!")