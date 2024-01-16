# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:59:30 2024

@author: 2406
"""

name = input("Enter your name:")
weight = int(input("Enter your weight in pounds:"))

height = int(input("Enter you height in inches:"))

BMI = (weight * 703 ) /(height * weight)

print(BMI)

if BMI>0:
    if(BMI<18.5):
        print(name +", You are underweight.")
    elif(BMI<=24.8):
        print(name +", You are normal weight.")
    elif(BMI<=34.8):
        print(name +", You are overweight.")
    elif(BMI<=34.8):
        print(name +", You are severely obese.")
    else:
        print("Enter valid input")
        
        