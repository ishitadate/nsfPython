# NSF Week 6 Class Notes

print("Homework 5 Review")
# Question 1
""" 
Question 1
If I give you a list, write something that creates a new list that contains only the first list's unique elements, 
no duplicates.
"""
listOne = [1,2,4,3,1,1,1,5,6,3,3,2,6,4,6,7]
newList = []
for x in listOne:
    if x not in newList:
        newList.append(x)
print(newList)

# Question 2
""" 
Question 2
If I give you a list, write something that will remove all duplicates.
DIFFERENCE BETWEEN Q1 and 2: you are changing the original list here, not creating a new one.
"""
listTwo = [1,2,4,3,1,1,1,5,6,3,3,2,6,4,6,7]
print(list(set(listTwo)))

# -----------
print("Lesson")
print("Intro to functions")
# Definition: a piece of code written to carry out a specified task.
# Use: to bundle a set of instructions that you want to use repeatedly or that, because of their complexity, 
#   are better self-contained in a sub-program and called when needed.
# Functions are able to take in values and return values back
# Input and output options: the function might or might not need multiple inputs. When the task is carried out, the 
#   function may or may not return one or more values.

# -----------
print("Types of functions")
# built-in functions: examples include print() and append()
# user-defined functions: users create functions using the "def" keyword to make their own program better
# anonymous/lambda functions: not declared with the standard "def" keyword

# -----------
print("User-defined functions")
# first, let's talk about parameters
    # information that you can pass to the function
    # you can put in as many as you want, just separate them by commas
    # when you are defining the function, the parameters are represented by basically variable names
    # you use these same names to reference the parameters in the function body
    # when you actually use the function, the real information you pass in will replace every time you used that variable
# next, let's talk about return statements
    # if you want to use the results of a function to do something else, you need to return those results
    # the way you would do that is by putting a return statement at the end
    # return statements are the last thing to be executed in a function
# four steps to creating a function yourself:
    # 1. use the keyword "def" and then put the name you want to give to your function
    # 2. add parameters to your function between the parentheses (if you have no parameters just leave the parentheses empty)
    # 3. put in the body of your function (what you want it to do)
    # 4. end with a return statement if you want it to return something; no return statement will return an object None
# no parameters, no return statement example
def hello():
    print("Hello World")
# yes parameters, no return statement example
def helloTwo(name):
    print("Hello " + name)
# yes parameters, yes return statement example
def helloThree(name):
    print("Hello " + name + " how are you")
    return True
# at this point, we've defined these functions, but they won't do anything because they haven't been called
# unlike regular code that runs from top to bottom, if you have a function, it won't run unless it's called somewhere else in the program
# the way you call a function is by writing out its name with parentheses and any parameters
# when you call the function, the code will execute, and any return statements will come back to you when it returns to where you called it from
hello()
helloTwo("Suhani")
print(helloThree("Suhani"))
# default parameters
    # you can set a default input that will be used if the user does not call the function with a value for that parameter
def food(favorite="pizza"):
    print("My favorite food is " + favorite)
    # here we've defined a function with a default parameter. if you don't put in any input when you call the function,
    # it will use pizza as the input. otherwise, it will use your input.
food("Chipotle")
food()
# using the return statement
    # think about it like this: the returned value replaces the function call when you come back to execute the rest of the program
def returnFunction(name):
    return "Hi " + name
print(returnFunction("Suhani") + ", how are you?")
    # the "Hi " + name (what was returned from the function) is what was printed in place of the call

# -----------
print("Lambda functions")
# a small anonymous function (called that because it doesn't use the keyword "def" to be defined)
# useful for just quick, small uses
# can take any number of arguments but only has one expression
# returns the result of that one expression
# syntax: variable = lambda arguments: expression
x = lambda a: a + 10
print(x(5)) # prints the result of putting in 5 as a in the lambda function above
# why use lambda functions?
    # the power of lambda is better shown when you use them as an anonymous function inside another function.
    # say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def multiply(n):
    return lambda a: a * n
    # Use that function definition to make a function that always doubles the number you send in:
mydoubler = multiply(2) # this is basically giving you the ability to make a function that returns a * 2
print(mydoubler(11)) # the parameter you pass into mydoubler represents a
    # now you can change the number by just making a new statement with a different parameter into myfunc
mytripler = multiply(3)

# -----------
print("Why are functions useful?")
# makes code modular and reusable
# if you want to do the same thing 10 times but at different points in your program, you could copy and paste 10 times, but that's so inefficient
# if you just define a function that does the same thing, you only have to write the statements once and then just call it whenever you need
# also makes it easier to change things
# imagine if you realized you had to change values you used throughout your program, you would have to do it individually for every time you copy-pasted
# with functions, you can just change the value of the parameter, making it so much easier
# you also only have to change the function body once if you need to change something about the way the program executes

# -----------
print("Student examples")
# Question 1: Write a function that inputs two numbers and prints the sum and the product.
def math(a,b):
    print("the sum is " + str(a+b) + " and the product is " + str(a*b))
# Question 2: Write a function that inputs length and width and prints the area of a rectangle.
def area(length, width):
    print("the area of the rectangle with length " + str(length) + " and width " + str(width) + " is "+ str(length*width))
# Question 3: change both the homework questions from last week into functions
# functions can be more complicated than the ones defined above. 
    # for example, we can use for loops, conditional statements, and more within our function block.
# Question 4: define a function to check if the name inputted has a vowel in it
def vowel(name):
    for x in name.lower():
        for letter in ['a', 'e', 'i', 'o', 'u']:
            if x == letter:
                return "Your name has a vowel"
    return "Your name does not have a vowel"
print(vowel("Suhani"))
print(vowel("bcd"))