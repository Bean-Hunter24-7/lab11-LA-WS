"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

# First example
class Calculator:
    def add(a, b): 
        return a + b
    def subtract(a, b):
        return a - b
    def mul(a, b):
        return a * b
    def div(a, b):
        return a / b
    def logarithm (a, b):
        return math.log(a, b)
    def exp(a, b):
        return a ** b
    def hypotenuse(a, b):
        return a ** 2 + b ** 2
    def square_root(a):
        return math.sqrt(a)

