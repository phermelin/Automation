#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 12:04:04 2025

@author: peter
"""

#def UserRole (lineOfInfo):
# the first section is the users Role
import array


counter =0
x=""
z=0
y=[]

with open ('loginInput.txt','r') as file:
    for line in file:
        y = line.split(',')
        print(y[0])
        print(y[1])
        gg = y[2]
        gg = gg[:-1] # removes the \n at the end of the last colunn
        print(gg)
