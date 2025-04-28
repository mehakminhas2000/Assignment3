Task 1: Calculate Factorial Using a Function 
Problem Statement: 
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
 
def factorial(n):
    if n <2:
        return 1
    else:
        return n * (factorial(n-1))
n = int(input("Enter a number: "))
result = factorial(n)

print("Factorial of",n,"is:",result)

output - Enter a number: 5
         Factorial of 5 is: 120

Task 2: Using the Math Module for Calculations
Problem Statement:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results

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

Output - Enter a number: 25
         Square root: 5.0
         Logarithm: 3.2188758248682006
         Sine: -0.13235175009777303

