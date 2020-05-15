# NSF Week 2 Notes

# Review:
# - Commenting (highlight cells)
#   - Mac: "cmd" + "/"
#   - Windows: "ctrl" + "k" + "ctrl" + "c"
#   - repl: "f1" + type "toggle line comment"

# ls - what is in the directory now
# cd - navigate to next directory

# Operations:
# - Numbers
#   - Add
#   - Subtract
#   - Multiplication
#   - Division
#   - Integer division

print(5/3)
print(5//3)

#   - Modulus

# % remainder
print(5 % 3)

# - Strings
# str is a type, str1 is NOT a type

#   - + and *
# concatanation = combining words

str1 = "Ishita"
print(str1 + " is the best" + " NOT")

str2 = "phone"
print(str2 * 4)

#   - - and /
# you can not use - and / with a string, this will lead to an error

# str3 = "mug"
# goal = "ug"

# print(str3 - "m")

# - Combining Operators with Assignment
# +=
# -=
# *=
# /=

apples = 6
apples - 3

print("apples " + str(apples))

banana = 6
banana -= 3

print("banana " + str(banana))


# casting = help the computer compile
# str(the variable that you want to cast)

var1 = 7
print("python reads this as a string " + str(var1))

# - Comparison Operators
# = is assignment
# Example : var1 = 7

# == is equality
print("8 == 8", 8 == 8)

# != is inequality
print("8 != 2", 8 != 2)

# < and > is the same as algebra class

print("8 =< 8", 8 <= 8)

# <= and >= is the same, make sure that the equals sign is on the right
# uncomment the next line to see the error
# print("8 =< 8 is bad syntax", 8 =< 8)

# If/Else:
# - Basic Structure

# if condition:
#   what to do
# else:
#   what to do

# this should print var1
var1 = 4

if var1 == 4:
  print(var1)
else:
  print("false")

# this should print "false"
var1 = 7

if var1 == 4:
  print(var1)
else:
  print("false")

# - Elif
# in one block, only one if statement and one else statement can exist. otherwise you get an error. 
# elif does the same thing as an if, but you have an unlimited number of them
#   an elif ALWAYS needs to follow an if

# if condition:
#   do stuff
# elif condition:
#   do stuff
# else:
#   do stuff

# - Keywords
#   - pass = placeholder... tells python to move on

# this would not compile:
# if condition:
# else:

# if condition:
#   pass
# else:

#   - break: breaks out of the if statement. we will use this with nested loops

# Input from User:
# - Built in python methods
#   - https://docs.python.org/3/library/functions.html

number = input("give a number ")

if int(number) == 4:
  print("good job")
elif int(number) == 5:
  print("do better")
else:
  print("try again")

