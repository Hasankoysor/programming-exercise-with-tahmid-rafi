# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 01:31:14 2022

@author: MD KOYSOR HASAN
"""

tiket_prize = int(input())
in_my_poket = int(input())

if in_my_poket >= tiket_prize:
    print("I can go to museum!")
    print("Nobody can stop me cz i have Tiket!")
if in_my_poket < tiket_prize:
    print("You need a Tiket!")