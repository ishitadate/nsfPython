import unittest
""" 
To Do: For each problem, replace the question variable with the python type of the answer. 
The variables have been instantiated with 'False' so the program will run.

Example: Question A
	
	a = 5 + 3
	typeA = 

Answer: Question A
	
	a = 5 + 3
	typeA = int

"""

# Question 1

number_1 = "six"
type_1 = str 

# Question 2

number_2 = 5 + 6
type_2 = int 

# Question 3

number_3 = 12 // 5
type_3 = int 

# Question 4

number_4 = 3.1 * 4
type_4 = float 

# Question 5

number_5 = 4 == 6
type_5 = bool 


# Tests ... do not edit
class TestStringMethods(unittest.TestCase):

    def test_question_1(self):
    	message = "Question 1 is incorrect"
    	self.assertEqual(type(number_1), type_1, message)

    def test_question_2(self):
    	message = "Question 2 is incorrect"
    	self.assertEqual(type(number_2), type_2, message)

    def test_question_3(self):
    	message = "Question 3 is incorrect"
    	self.assertEqual(type(number_3), type_3, message)

    def test_question_4(self):
    	message = "Question 4 is incorrect"
    	self.assertEqual(type(number_4), type_4, message)

    def test_question_5(self):
    	message = "Question 5 is incorrect"
    	self.assertEqual(type(number_5), type_5, message)


if __name__ == '__main__':
    unittest.main()








