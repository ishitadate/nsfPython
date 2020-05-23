# Week 2 Solutions

# 1. // is integer division. It takes the floor of a number.

# 2. % is a  modulus. It finds the remainder of the division between numbers.

# 3. Apples is not updated in memory. It should read:

apples = 6
apples -= 3

# 4. Ilikecookies

# 5. Yes. You can't subtract from a string, this is a syntax error.

# 6. !=

# 7. Sample code. Keep in mind there are multiple ways to write this solution.

number = 5

userInput = int(input("Pick a number "))

if userInput < number:
  print("guess higher")
elif userInput > number:
  print("guess lower")
else:
  print("good job")