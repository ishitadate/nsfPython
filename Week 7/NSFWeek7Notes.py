# NSF Week 7 Class Notes

print("Homework 6 Review")
"""
Question 1
Write a function that takes in two numbers and finds the difference between their sum and their product. 
Name the function sum_diff and have it return an integer.

Sample input: 4,5
Expected output: -11
"""
def sum_diff(num1, num2):
    return ((num1+num2)-(num1*num2))
print(sum_diff(4,5))

"""
Question 2
Write a function that takes in three numbers and returns the maximum of the three numbers. Name the function findMax.

Sample input: [2,5,4]
Expected output: 5
"""
def findMax(num1, num2, num3):
    maxNum = 0
    for x in [num1, num2, num3]:
        if maxNum < x:
            maxNum = x
    return maxNum
print(findMax(2,5,4))

"""
Question 3: Challenge
Write a function that determines whether a number is prime. Name this function is_prime, and make it return 
either true or false.
"""
def is_prime(num):
    for x in range(2, num):
        if num%x == 0:
            return False
    return True
print(is_prime(4))
print(is_prime(3))

# -----------
print("Lesson")
print("Intro to dictionaries")
# also known as a hash map
# Definition: a collection of data that has pairs of "keys" and "values"
# similar to a list because you're able to store a group of data but instead of using indexes to keep track of 
    # items you use the keys
# think of it like a two-column table
# useful for paired data
# dictionaries are enclosed in curly braces, in which you put the key, then the colon, then the value associated with it
# to access the value at a certain key, use square brackets, just like a list (or the get() method)
# be careful! dictionaries are unsorted, which means they don't store the information in any particular order
car = {"brand": "Tesla", "model": "Y", "year": 2020}
print(car["brand"])
print(car.get("brand"))

print("Dictionary operations")
# to add, just put your new key in square brackets and set the new value
car["owner"] = "suhani"
# to remove, use the keyword del
del car["owner"]
# to check if something is in the dictionary by key
if "owner" in car:
    print("yes")
else:
    print("deleted")
# to check if a certain value is in the dictionary
# car.values() returns a list of all values (in this case, ["Tesla", "Y", 2020])
if "Tesla" in car.values():
    print("cool") # cannot get the key from here though
# iterate through a dictionary
for key in car:
    print(car[key]) # this will print all the values
# get the length (returns the number of key-value pairs)
len(car)

print("Dictionary vs list")
# lists are ordered. list_name[0] returns something if the list isn’t empty. dictionary_name[0] isn’t a thing.
# in dictionaries, values are paired with keys. this isn’t the case with lists. 

print("Student example 1")
# Write a function that will add a given value with a given key only if that key does not already exist in the dictionary.
d = {}
def add(key, value):
    if key not in d:
        d[key] = value

print("Student example 2")
# How can you use a dictionary to create a sample grocery list?
# answer: keys are the items, values are the amounts of each item

print("Student example 3")
# Write a Python program to combine two lists into 1 dictionary.
def combine(keys, values):
  dictionary = {}
  for x in range (0, len(keys)):
    dictionary[keys[x]] = values[x]
  return dictionary

newDictionary = combine([],[])

print("Student example 4")
# write a program to print all unique values in a dictionary
# a function that takes in a dictionary and returns a list of all the unique values

def unique(dictionary):
  newList = []
  for x in dictionary.values():
    if x not in newList:
      newList.append(x)
  return newList

print("Student example 5")
"""
You run a fruit store, and you sell oranges, apples, bananas, papayas, and pears. Write a dictionary of all the 
items and how much they cost, and write another dictionary with the same items and how many you have. 
How much would you earn if you sold everything?
How much would you earn if you sold only the apples?
How much would you earn if you sold the items whose names start with “p”?
"""
prices = {"oranges": 1, "apples": 2,"bananas": 3, "papayas": 4, "pears":5}
amounts = {"oranges": 5, "apples": 4, "bananas": 3, "papayas": 2, "pears": 1}

#Q1
total = 0
for x in prices.values():
  total+=x
for key in prices:
  total+=prices[key]
print(total)
#Q2
print(amounts["apples"]*prices["apples"])
#Q3
newTotal = 0
for key in prices:
  if key.lower().startswith('p'):
    newTotal+= prices[key]*amounts[key]
print(newTotal)