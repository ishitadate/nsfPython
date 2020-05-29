# Week 3 Solutions

# 1. A for loop runs for a finite amount of time. A while loop will run infinitely until you tell it to stop.

# 2. output:

0
1
2
3


# 3. this code will print "x is less than 3" infinitely 

# 4. output:

5
6
7
8


""" 
Number One:
Using a for loop, output how many odd and even integers are in the following list.
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
"""
print("Number 1")
numbersOne = (1, 2, 3, 4, 5, 6, 7, 8, 9) 

oddInts, evenInts = 0, 0

for i in range(len(numbersOne)):
	if numbersOne[i] % 2 == 0:
		evenInts += 1
	else:
		oddInts +=1

print("odd ints: " + str(oddInts) + "; even ints: " + str(evenInts))

""" 
Number Two:
Using a for loop, find the maximum of the following list
Expected Output :
Maximum : 10
"""
print("\nNumber 2")
numbersTwo = (1, -5, 3, 4, 10, 8, -9) 

currMax = numbersTwo[0]

for num in numbersTwo:
	if currMax < num:
		currMax = num

print("maximum:", currMax)

