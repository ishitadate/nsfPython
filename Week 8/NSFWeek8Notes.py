# NSF Week 8 Class Notes

print("Homework 7 Review")
"""
Question 1
Create a dictionary with 3 students. Each student has a grade for each of their 5 subjects as well as a list of
supplies in their bag. What is the best data structure to manage all of this?
"""
# answer: create a nested dictonary!
school = {
    "student1": {
        "grades": {
            "history": 99,
            "english": 100,
            "math": 98,
            "science": 99,
            "gym": 100
        },
        "supplies": ["pens", "pencils", "textbooks", "notebooks", "binders"]
    },
    "student2": {
        "grades": {
            "history": 99,
            "english": 100,
            "math": 98,
            "science": 99,
            "gym": 100
        },
        "supplies": ["pens", "pencils", "textbooks", "notebooks", "binders"]
    },
    "student3": {
        "grades": {
            "history": 99,
            "english": 100,
            "math": 98,
            "science": 99,
            "gym": 100
        },
        "supplies": ["pens", "pencils", "textbooks", "notebooks", "binders"]
    }
}

"""
Question 2
Rename a key in a dictionary.
"""
# sample input
sampleDict = {
  "name": "Raj",
  "age": 25,
  "salary": 8000,
  "city": "New York"
}
# answer
sampleDict["location"] = sampleDict.pop("city")

"""
Question 3: Challenge
Write a function to invert a dictionary. It should accept a dictionary as a parameter and return a dictionary where the 
keys are values from the input dictionary and the values are lists of keys from the input dictionary.
"""
# sample input
d = { "key1" : "value1", "key2" : "value2", "key3" : "value1" }
# expected output
# output = { "value1" : ["key1", "key3"], "value2" : ["key2"] }

output = {}
for x in d.keys():
    if d[x] not in output:
        output[d[x]] = [x]
    else:
        output[d[x]].append(x)
print(output)

# -----------
print("Lesson")
print("Intro to files")
# why would we use files?
    # Sometimes it’s useful to give our user input as a file. For example, if I was to have a very large input, 
    #   instead of typing it out every time I test my program, I can just read the file. 
    # Also, what if you have multiple prompts and want to keep all your answers the same, for testing purposes 
    #   or otherwise? It’s easier to read from a file. 

print("Objects")
# Python is an object-oriented programming language. That means that programmers use classes to organize objects. 
# This is an example of a “car” class that can be used to create multiple different “car” objects, each with 
#   different properties. 
# The class provides a template and instructions as to how to create objects and what to do with them. 
# The class also has functions, which tell us what we can do with the object. For example, if we have a “car” 
#   object named volvo, we can write: volvo.setSpeed() to get the speed of the volvo object. 
# If I have another car honda, the same line will not change the honda’s speed.

print("Back to files")
# Let’s say we have a file called carnames.txt. So, what we do is create a file object called f and use the 
#   function open():
f = open("carnames.txt", "r")
# (carnames.txt has to be in the same folder as our current python program). 
# Let’s get the content of the file and print it out:
file_contents = f.read() #(string)
print(file_contents)
# How about reading just the first line?
first_line = f.readline()
second_line = f.readline()
print(second_line)
# So, when we open a file, we have to close it, right?
# Option 1: use open() to open a file, and when you’re done with it, use close() to close the file. 
f = open("carnames.txt","r")
f_text = f.read()
f.close()
# We don’t have to worry about using close() when we’re done if we use the with keyword:
with open("carnames.txt", "r") as f:
    # do the stuff about the file f in here.(remember to indent!)
    print(f.readline())

print("student challenge")
# Use the with keyword to print an entire file, line by line. 
with open("carnames.txt", "r") as f:
    f_line = f.readline()
    while (f_line != ""):
        print(f_line)
        f_line = f.readline()

print("Writing to a file")
# First, let’s open the text file, as usual, but this time we tell python we’ll be writing in the file:
f = open("carnames.txt", "w")
# We use write() to write to the file:
f.write("This is some new text in the file.")
f.close()

