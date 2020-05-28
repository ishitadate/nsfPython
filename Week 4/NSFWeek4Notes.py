# NSFWeek4Notes.py

# repl.it issues will be addressed at the end of class

# Homework 3 Review

""" 
Number One:
Using a for loop, output how many odd and even integers are in the following list.
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
"""
print("Number 1")
numbersOne = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

expectedEven = 5
expectedOdd = 4

countEven = 0
countOdd = 0 

for i in range(len(numbersOne)): #this gives [0,1,2,3,4,5,6,7,8]
  var1 = i
  if numbersOne[i] % 2 == 0:
    countEven += 1
  else:
    countOdd += 1

print("even numbers: ", countEven)
print("odd numbers: ", countOdd)

""" 
Number Two:
Using a for loop, find the maximum of the following list
Expected Output :
Maximum : 10
"""
print("Number 2")
numbersTwo = (1, -5, 3, 4, 10, 8, -9) 

greaterVal = numbersTwo[0]

for i in range(len(numbersTwo)):
  currTerm = numbersTwo[i]
  if greaterVal < currTerm:
    greaterVal = currTerm

print("maximum", greaterVal)

""" 
Number Three:
Using a for loop, find the minimum of the following list
Expected Output :
Maximum : -9
"""
print("Number 2")
numbersTwo = (1, -5, 3, 4, 10, 8, -9) 

currLeast = 100000000000

for i in numbersTwo:
  if i < currLeast:
    currLeast = i

print("minimum", currLeast)


# ---------

print("Strings")
# - collection of alphabets, words, or other characters
#   - a bunch of characters put together
# - primitive data structures
# - building block for data manipulation
# - string is defined by single quote or a double quote "" or ''
# char = character = letter = digit = % = $

# ---------

print("String operations (review)")
# - concatation: putting strings together using + operator
# - * same as algebra... does concatantion that many times

aStr = "cookies"
print(aStr + " are good")
print(aStr * 3)

# ---------

print("Accessing characters in a string")

# - Indexing
aString = "computer"
print(aString[0]) 
# - indexing begins at 0
  # aka... the first character is at index 0
# - can not access a character out of range
  # print(aString[10])
# indexing is done with ints
  #print(aString[1.5])

# - Negative Indexing
aString = "computer"
print(aString[-1])
# all the rules about indexing apply for negative and positive numbers

# - Range
aString = "computer"
print(aString[0:3]) # index char 0, char 1, char 2
  # the last number is exclusive
  # the first number is inclusive

# the : is called the slicing operator
# putting it at the beginning or end, will give you the rest of the string

print(aString[3:])
print(aString[:3])

# Student Example
print("student example 1")

aStr = "Hello World"

# print the first char of the word using two differrent methods
print(aStr[0])
print(aStr[:1])
print(aStr[-11])
# print the first three chars of the word
print(aStr[:3])
# print the last four chars of the word
print(aStr[-4:])
# print all but the first 5 chars
print(aStr[5:])
# ---------

# Testing Strings: functions written into python that output a bool
# Check out "https://docs.python.org/2.5/lib/string-methods.html" for more!

# syntax: string . name of the function ()
# is alpha
print("is alpha")
aString = "24"
print(aString.isalpha())
aString2 = "ishita"
print(aString2.isalpha())

# is digit
print("is digit")
aString = "24"
print(aString.isdigit())
aString2 = "ish56ita"
print(aString2.isdigit())

# is isalnum() ... checks whether it is either alphabetic or numerical
print("isalnum")
aString2 = "ish56%ita"
print(aString2.isalnum())

# is upper... checks for uppercase
# is lower... checks for lowercase

# parameter is an input to the function
  # aka it's what goes inside the parentheses

# endswith ... it sees if the last char is equal to the parameter
print("endswith")
aString3 = "ishita"
print(aString3.endswith("5"))

#startswith .. works the same but at the beginning

# Example

print("Student Example 2")

aStr1 = "summer is "
aStr2 = "100%"
aStr3 = " the best"

"""
We want to combine the strings, only if the format is what we want...
1. String 1 is only alphabetic 
# 2. String 2
# 	a. The last char is %
# 	b. The rest of the chars are numeric
3. String 3 is lowercase

Write nested if statements to check these conditions, if they are all true, print the concatanation.
"""

if aStr1.replace(" ", "").isalpha():
  if aStr2.endswith("%") and aStr2[:-1].isdigit():
    if aStr3.islower():
      print(aStr1 + aStr2 + aStr3)
else:
  print("did not work")


# ---------

# Other string functions

# - Strip removes whitespace BEFORE or AFTER a word... not in the middle
print("strip")
aString = "     word"
print(aString.strip())

aString = "     word  another word     "
print(aString.strip())

# - Upper and Lower
print("upper and lower")

upperString = "ABCD"
print(upperString.lower())

lowerString = "defg"
print(lowerString.upper())

lowerString = "defgWORD"
print(lowerString.upper())
