"""
Question 1
Create a dictionary with 3 students. Each student has a grade for each of their 5 subjects as well as a list of
supplies in their bag. What is the best data structure to manage all of this?
"""

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
# expected output ("city" --> "location")
{
  "name": "Raj",
  "age": 25,
  "salary": 8000,
  "location": "New York"
}

"""
Question 3: Challenge
Write a function to invert a dictionary. It should accept a dictionary as a parameter and return a dictionary where the 
keys are values from the input dictionary and the values are lists of keys from the input dictionary.
"""
# sample input
d = { "key1" : "value1", "key2" : "value2", "key3" : "value1" }
# expected output
output = { "value1" : ["key1", "key3"], "value2" : ["key2"] }