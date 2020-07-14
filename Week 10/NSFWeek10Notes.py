# NSF Week 10 Notes

print("Homework 9 Review")

print("Lesson: Recursion")
# Introduction: factorial
# do you guys all know what a factorial is?
# basically you take a number and you multiply it by all the numbers less than it
# every time, you have to take the number and multiply it by 1 less than it and then 
#   multiply that by 1 less than the last number and so on
# with all the stuff that we have learned so far (loops, if statements, and functions),
#   can you think of a way to evaluate the factorial of any number?
# is it possible to write something really simple and nice function to do this
# 0! by definition is 1
# 1! = 1 * 0!
# 2! = 2 * 1!
# 3! = 3 * 2! and so on
# if you break down this problem into it's very core, it's smallest portion,
#   you're basically doing the same thing several times over: 
#   multiplying a number by the factorial of the number one less than it
# but we're trying to write a function to evaluate a factorial, 
#   so what use is it if our solution has a factorial in it??
# so now what if, you could have that function call itself???

# Overview
# what is recursion? formal definition is a function defined in terms of itself using self-referential expressions
# what does that mean? basically it's a function that calls itself
# there are 2 things it needs: a statement calling the function itself and a stop condition ("base case")
# basically, it keeps calling the function itself until it reaches a stop condition
# when it reaches the stop condition, it goes back up backwards
# the reason for this is that when it reaches the stop condition, the program then returns to complete the most recently invoked previous call
# when you hit a return statement in a program, you immediately go to the result of that return statement, even if there's still stuff left to do in the function
# when you finally hit the "base case", the program then goes back up to complete the other calls it didn't, going in the order of the most recent one
# when you reach the stop condition, you still have to go back up to complete everything else
# let's do an example to clear this up a bit.

# Example 1: Factorial
def factorial(number):
    if(number == 0):
        return 1
    else:
        return number * factorial(number-1)
print(factorial(5))

# Tracing table
"""
what is?         | return           | recursion
factorial(5)     | 5 * factorial(4) | # this is a recursive statement. right now, we have no idea what factorial(4) is
factorial(4)     | 4 * factorial(3) | # no idea what factorial(3) is
factorial(3)     | 3 * factorial(2) | # no idea what factorial(2) is
factorial(2)     | 2 * factorial(1) | # no idea what factorial(1) is
factorial(1)     | 1 * factorial(0) | 
factorial(0)     | 1 # YAY          |

what is?         | return           | recursion
factorial(5)     | 5 * factorial(4) | 5 * 24 = 120
factorial(4)     | 4 * factorial(3) | 4 * 6 = 24
factorial(3)     | 3 * factorial(2) | 3 * 2 = 6
factorial(2)     | 2 * factorial(1) | 2 * 1 = 2
factorial(1)     | 1 * factorial(0) | 1 * 1 = 1
factorial(0)     | 1 # YAY          | 1
"""

# Be careful! Stack overflow
"""
def f(number):
    if(number == 100):
        return 1
    else:
        return number * f(number-1)
print(f(5))
"""
# be careful what you put as your base case
# in this function, it's all the same as our previous one except the base case is 100
# that may never be reached, and the function will just keep calling itself,
#   leading to something called a stack overflow
# the recursive function calls are stored in something called a stack, enabling the function to
#   go back and finish up once the base case is reached
# if it's never reached, though, you'll create something never-ending

# Another example: recursion without a return statement
def divide(num):
    if (num >= 10):
        divide(num//9)
    
    print(num%10)

divide(109)

"""
current num      | new argument                 | print
109              | 109 // 9 = 12                | 109 % 10 = 9
12               | 12 // 9 = 1                  | 12 % 10 = 2
1                | # 1 < 10 so start printing   | 1 % 10 = 1
"""

# Trace this (make a table, on a Google doc or something if it's easier)
def one(x):
    if (x == 0):
        return 1
    else:
        return 2 * one(x-1)
print(one(5))

def two(y):
    if (y >= 7):
        return 1
    else:
        return two(y + 2) + two(y + 1)
print(two(4))

def three(z):
    print(z % 10)
    if ((z // 10) != 0):
        three(z // 12)
    else:
        print(z % 5)
three(99)

def four(n):
    print(n % 10)
    if ((n // 10) != 0):
        four(n // 12)
    print(n % 5)
four(99)

# Practice Examples

# 1: write a recursive function to model the Fibonacci sequence
def fib(num):
    if (num == 0):
        return 0
    elif (num == 1):
        return 1
    else:
        return fib(num-1)+fib(num-2)
print(fib(10))

# 2: write a recursive function to print a string backwards
def backwards(string):
    if (len(string) > 1):
        backwards(string[1:])
    print(string[0])

backwards("109")