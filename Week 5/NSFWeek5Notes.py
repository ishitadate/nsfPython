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
    # - listName[index]
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
    # - listName[index] = somethingelse
    # - it will replace what is currently there
    # - cannot use it to add values, because the index will be out of bounds
myName[1] = 'o'
print(myName) # will print [s, o, h, a, n, i]
myName[1] = 'u'
# - you can see that a list index behaves like any other variable name (access and assign)
print("Student example 1")
# - 3 ways to access the 4th item in the array
myName[3]
myName[-3]
myName[3:4]

# -----------
print("List length and adding")
# - in python, lists don't have a set length
# - to find out how long a list is just use len(); ex. len(listName)
print (len(myName)) # should print 6, because there are 6 items in this list
# - to add use .append(); ex. list.append(newItem)
# - by default this adds to the end
myName.append('b')
print(myName) # should print [s, u, h, a, n, i, b]
# - to insert at a specific position, use .insert(); ex. listName.insert(index, newItem)
# - this will push everything after that index over 1
myName.insert(6, ' ')
print(myName)
# - to add multiple items at once, use .extend(); ex. listName.extend([item1, item2, item3])
myName.extend([3,4,3])
print(myName) # should print [s, u, h, a, n, i, , b, 3, 4, 3]
# - there is a fourth way to add to a list! concatenation
print(myName + [7,0]) # should print [s, u, h, a, n, i, , b, 3, 4, 3, 7, 0]
print(myName) # original list unchanged; should print [s, u, h, a, n, i, , b, 3, 4, 3]
print("Student Example 2")
# write a way to add every character from a string into a list as a separate item
subject = "python"
subjectList = []
for char in subject:
    subjectList.append(char)
print(subjectList)
subjectList2 = list(subject)
print(subjectList2)

# -----------
print("Remove from a list")
# - using del
    # - to delete an item at a known index: del listName[index]
    # - to delete a range of items: del listName[startIndex:endIndex]; again endIndex not included
    # - to delete the entire list: del listName
# - using .remove()
    # - removes a given item (you are providing the value of the item here, not the index)
    # - listName.remove(item)
# - using .pop()
    # - if you provide an index, it will remove the element at that index
    # - if you don't provide an index, it will remove the last element
    # - .pop() returns the element that was removed
# - QUESTION: in what scenarios should you use each way to remove something? 

# -----------
print("Searching a list")
# - use a regular for loop to check if something is in a list
print("Student Example 3")
for i in range(0, len(myName)):
    if myName[i] == 'o':
        print("you spelled it wrong :(")
# - can also use if ... in
if 'o' in myName:
    print("you spelled it wrong :(")