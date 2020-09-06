# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 14:09:42 2020

@author: Sourav Singh
"""


for Number in range (1, 200):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '\n ')
