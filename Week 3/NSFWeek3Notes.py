# NSFWeek3Notes.py

# repl.it review
# - make new repl and use the "run" button
# 	- backend code to interpret as a python file
# 	- similar to an IDE
# - use the class links for the github repo

# homework review/questions

# nested if statements: if statement within another if statement

# var1 = 8
# var2 = 10

# if var1 > 0:
#   if var1 < var2:
#     print("true")

# if var1 > 0 and var1 < var2:
#   print("true")
#   print("yay")

# if not var1 < 0 and var1 < var2:
#   print("true")

# -----

# Loops: repeat lines of code
print("corn")
print("corn")
print("corn")

# Logic
# 1. check condition
# 2. if true, then it will execute the body of the loop, then go back to step
# 3. if false


# Types of Loops (basic)
# while loop: repeat a statement infinetely, while the conditional is true
print("start loop")

counter = -30
while counter > 0:
  print("corn")
  counter -= 1

# else along with while... another way to write what is above

counter = -30
while counter > 0:
  print("corn")
  counter -= 1
else:
  print("false")

# be careful of infinite loops. if the conditional is never updated, then the loop will run forever and you will get a runtime error

# for loop: will happen for a finite amount of time. always excutes

# for each
# iterable - examples: string "dog"
# list = [4, 5, 6, "string", True]
# int is not an example: 123 

animalList = ["hippo", "giraffe", "lion"]

for animal in animalList:
  print(animal)

# indexing at python starts at zero... the first element is referred to as the 0th element

# animalList[0] = "hippo"
# animalList[1] = "giraffe"

for index in range(3):
  print(animalList[index])

# range function

# range(start, stop, step)
# start - python assumes to 0
# stop - this you MUST input
# step - python assumes to be 1

# range(0, 5, 1) = [0 , 1 , 2 , 3 , 4]
# range(0, 5, 2) = [0 , 2 , 4]
# range(3) = [0, 1, 2]

for i in range(3):
  print(i)

# ---

# Student Example: create a sequence of numbers, 3 to 17, counting by 3's. print each of those numbers

for i in range(3, 17, 3):
  print(i)

# Student Example 2: take an input from the user for what their favorite food is. iterate through that word and print each of its letters on a seperate line

food = input("What is your favorite food?")
for letter in food:
  print(letter)

for i in range(len(food)):
  print(food[i])

# Nested loops:

for i in range(150):
  for j in range(5):
    print(i * j)

# the following is an infinite loop
# for i in range(4):
#   while(i < 2):
#     print("true")

# ---

# Loop control statements: change the execution from the normal sequence
# break = terminates the loop statement and transfers execution to the statement immediately following the loop
# if you are in a nested for loop, it only breaks out of the most inner for loop

string1 = "I like Pizza!"
for letter in string1:
  if letter == "z":
    break
  else:
    print(letter)

print("finished")

# continue cause the loop to skip over the remainder of its body and retest its condition

string1 = "I like Pizza!"
for letter in string1:
  if letter == "z":
    continue
  print(letter)

print("finished")

# pass: used when a statement is required syntaticially but you do not want anything to execute

for i in range(5):
  if i == 4:
    pass


# Example: Get a number from the user.
# 1. If the number is odd, print a countdown down to 0
# 2. If the number is even, print a countup to 15
#     2a. if number is greater than 15, give the uesr an error
#   2b. However, anytime you want to print the number 13, the user gives an error that says, "I can't handle 13"

var1 = input("Give me your number")
var1Int = int(var1)

if (var1Int % 2) != 0: #odd
  for item in range(var1Int, 0, -1):
    print(item)
else:
  if var1Int> 15:
    print("too big")
  for item in range(var1Int, 15, 1):
    if item == 13:
      print("I can't handle 13")
      break
    print(item)