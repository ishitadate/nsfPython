# NSFWeek5Notes.py

# Homework 4 Review
"""
Number One:
I have three strings, but I only want to combine the strings if the format is what I want...

1. String 1 is only alphabetic 
  2. String 2
 	a. The first char is $
 	b. The rest of the chars are numeric
3. String 3 is uppercase
"""

aStr1 = "MyPizzaCosts "
aStr2 = "$700"
aStr3 = " THATSALOT"

if aStr1.strip().isalpha():
    if aStr2.startswith('$'):
        if aStr2[1:].isdigit():
            if aStr3.isupper():
                print(aStr1 + aStr2 + aStr3)

"""
Number Two: Remove all the l's in oldString

Expected Output: 
the newstring is: itsathursday
"""
oldString = "lillLltslatlllhurLsdlayL"

# solution 1
newString = ""
for character in oldString:
    if character != 'l' and character != 'L':
        newString+=character
print("the newstring is: " + newString)

# solution 2
newString2 = oldString.replace('l', '')
newString2 = newString2.replace('L','')
print("the newstring is: " + newString2)


# Lesson
print("Introduction to lists")
# - datatype you can use to store a collection of info
# - stored in an order, all under one variable name
# - how to create a list? 
    # - the variable name
    # - equals
    # - square brackets []
# - initializing a list with empty brackets would mean you are creating an empty list
# - if you want to create a list with items in it, put those items separated by commas in the order you want in the brackets
myName = ['s', 'u', 'h', 'a', 'n', 'i']
# - you can put anything you want in a list: strings, characters, integers, booleans, even other lists!
# - can mix datatypes in your list

# -----------
print("Using the index")
# - index starts from 0
# - access information
    # - list[index]
    # - can use this to give other variables the value stored at that index
print(myName[2]) # should print the third letter in my name, 'h'
fourthLetter = myName[3] # assigning another variable the value at index 3 of the list myName
print(fourthLetter) # should print the fourth letter in my name, 'a'
    # - access characters from the back: use a negative index (only works in python)
print(myName[-1]) # should print the last letter in my name, 'i'
    # - take out a part of the list, referenced by indexes
    # - includes the first index you specify, but not the last one
    # - returns a new list of just that section, does not affect the original list
print(myName[2:4]) # should print ['h', 'a']
# - assign values
    # - list[index] = somethingelse
    # - it will replace what is currently there
    # - cannot use it to add values, because the index will be out of bounds
myName[1] = 'o'
print(myName) # will print [s, o, h, a, n, i]
myName[1] = 'u'
# - you can see that a list index behaves like any other variable name (access and assign)

# -----------
print("List length and adding")
# - in python, lists don't have a set length
# - to find out how long a list is just use len(); ex. len(list)
print (len(myName)) # should print 6, because there are 6 items in this list
# - to add use .append(); ex. list.append(newItem)
# - by default this adds to the end
myName.append('b')
print(myName) # should print [s, u, h, a, n, i, b]
# - to insert at a specific position, use .insert(); ex. list.insert(index, newItem)
# - this will push everything after that index over 1
myName.insert(6, ' ')
print(myName)

# -----------
print("Searching a list")
# - use a regular for loop to check if something is in a list
print("Student Example 1")
for i in range(0, len(myName)):
    if myName[i] == 'o':
        print("you spelled it wrong :(")
# - can also use if ... in
if 'o' in myName:
    print("you spelled it wrong :(")


