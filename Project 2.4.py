"""
Project 2.4
Quentin Miller
"""
import math

#request the input

radius = float(input("Enter the sphere's radious: "))

#compute the results

diameter = 2 * radius
circumference = diameter * math.pi
surfaceArea = 4 * math.pi * radius * radius
volume = 4/3 * math.pi * radius * radius * radius 

#display the results

print("Diameter     :", diameter)
print("circumference:", circumference)
print("surface Area :", surfaceArea)
print("volume       :", volume)
