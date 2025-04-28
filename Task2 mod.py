#Task 2: Using the Math Module for Calculations

import math



def square(number):
        sqr = math.sqrt(number)
        print("Square root:",sqr)
def logarithm(number):
        log = math.log(number)
        print("Logarithm:",log)
def sine(number):
        sin = math.sin(number)
        print("Sine:", sin)
number = int(input("Enter a number: "))
square(number)
logarithm(number)
sine(number)
