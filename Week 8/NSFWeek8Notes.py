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
# this lesson is about input and output
# this is where we really start to add advanced functionality to our programs
# you can do so much more when you're able to take some material (input), manipulate it in a bunch of ways (process),
#   and then return that something to the user (output)

print("Intro to files")
# why would we use files?
    # Sometimes it's useful to give our user input as a file. For example, if I was to have a very large input,
    #   instead of typing it out every time I test my program, I can just read the file. 
    # Also, what if you have multiple prompts and want to keep all your answers the same, for testing purposes 
    #   or otherwise? It's easier to read from a file. 

print("open funtion")
# you have 3 operations you can do with a file: read, write, and append
# basically what determines what you're doing is how you use the open function
# there's an open function that allows you to open a file
# one of the parameters of the function lets you specify a mode, which basically means what you want to do with the file
# create a variable and assign it the result of the open function so that we can use that variable
# basically the variable is a file object, something we will talk about next week
# open function: variable = open("filename", "mode")

print("reading a file")
# the string to signify read mode is "r"
# file must be in the current folder
f = open("hello.txt", "r")
# Let's get the content of the file and print it out:
file_contents = f.read() #(string)
print(file_contents)
# How about reading just the first line?
first_line = f.readline()
second_line = f.readline()
print(second_line)

# So, when we open a file, we have to close it, right?
# Option 1: use open() to open a file, and when you're done with it, use close() to close the file. 
f = open("hello.txt","r")
f_text = f.read()
f.close()
# We don't have to worry about using close() when we're done if we use the with keyword:
with open("hello.txt", "r") as f:
    # do the stuff about the file f in here. (remember to indent!)
    print(f.readline())

print("Writing to a file")
# First, let's open the text file, as usual, but this time we tell python we'll be writing in the file:
f = open("hello.txt", "w")
# We use write() to write to the file:
f.write("HELLO")
f.close()
# using the write mode will overwrite anything that is already in the file
# if you change the string in the f.write on line 136, run the program again, and then check the file
# the text in the file would have changed completely
# use the mode w+ to be able to read and write
# meanwhile if the file doesn't exist, it creates the file

print("append")
# use append when you want to add to the bottom of a file and not write over what's already in the file
# mode is "a"
f = open("hello.txt", "a")
f.write("\n" + "i am appending this line")
f.close()
# if the file doesn't exist it creates the file

print("student examples")
print("example 1")
# Use the with keyword to print an entire file, line by line. 
with open("hello.txt", "r") as f:
    f_line = f.readline()
    while (f_line != ""):
        print(f_line)
        f_line = f.readline()

print("example 2")
# read the dictionary.txt file and assign it to a dictionary
f = open("dictionary.txt", "r")
d = {}
for line in f:
    temp = line.strip().split(",")
    d[temp[0]] = temp[1]
print(d)

print("example 3")
# take input from the command line and write it to a file
name = raw_input("What's your name? ")
with open("hello.txt", "a") as f:
    f.write("\n" + name)

print("CHALLENGE")
# make a game! make your own answer key file with the questions and correct answers
# have your program read the questions and send them to the user through the command line
# the program will read the user's answers and determine if it is right or wrong
# the program will write a file that says "right" or "wrong" for each question and a final score