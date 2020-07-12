# NSF Week 9 Notes

print("Homework Review")

print("Lesson")
print("Part 1: Object Oriented Programming")
"""
Volunteer 1: Anishka
the office room
walls: 4
ceiling: 1
door: 1
purpose: "quiet place to work"
furniture: desk, cabinets, two chairs, piano
special? yes, trophy case

Volunteer 2: Diksha
her bedroom
walls: 4
ceiling: 1
door: 3
purpose: "to sleep, work, relax"
furniture: bed, desk, chair, mirrors
special? yes, map and travel wall

Volunteer 3: Sai
his bedroom
walls: 8
ceiling: 1
door: 3
purpose: "to do homework, read, play, sleep"
furniture: bookshelves, desk, chair, bed
special? no

ROOM TEMPLATE
Room
integer walls
ceiling: 1
integer doors
string purpose
list furniture

class: template
object: item of that type
class is used to create object

class allows you to make user-defined data structures

object-oriented Programming
OOP is an approach for modeling concrete, real-world things, like rooms, as well as relations between things, 
like students and teachers. OOP models real-world entities as software objects that you can work with that have 
some data associated with them and can perform certain functions that are dictated by their class
"""

print("Part 2: Modules, Packages, Libraries")
# MODULES
# a module is just a file which contains various Python functions and global variables
# it is simply just a .py extension file which has python executable code
# Modules are used to break down large programs into small manageable logic units and organized files
# for example, say you're making a really complex game. you don't want all of the functions and everything 
# in the same file that controls the plot of your game and is the main runner file do you?
# it would get so crazy long, overwhelming, and messy
# instead, make modules to put in different functions
# ex. a module that is all about character movement
# another module that controls what happens when a character touches an object
# what you're doing is grouping like functions together and also getting rid of the clutter in your main file
# however, more importantly, modules provide reusability of code
# for example, if you wanted to create another game, but in this game, the characters moved the same way, 
# you could use the same module that you created the last time
# you can create modules yourself! the module name is the file name without the extension

# benefits of using modules
# besides making programs easier to read and use, there are a lot of benefits of using modules
# simplicity
#   Rather than focusing on the entire problem at hand, a module typically focuses on one relatively small portion of the problem
#   If you’re working on a single module, you’ll have a smaller problem domain to wrap your head around
#   This makes development easier and less error-prone
# maintainability
#   Code once written is bound to change in future because of the change in our business needs
#   having things organized into modules means that you only have to make changes in one place, not wherever you used the function
# reusability
#   Functionality defined in a single module can be easily reused by other parts of the application
#   This eliminates the need to recreate duplicate code.

# example of a module
# create a module
# import it all and use the . operator to access functions
# import one function
# import one function with an alias


# PACKAGES
# a package is a collection of modules
# in addition to a bunch of module files, it must contains an __init__.py file as a flag so that the python 
# interpreter processes it as such. 
# The __init__.py could be an empty file without causing issues, it's just needed for python to recognize it as a package
# generally some initilization code is put in it
# say your company is working on a huge application
# each team can create their own package of modules that can therefore also be used by everyone else working on it if its within the same project
# what's cool about packages is you can actually make packages and upload them to the python package index
# and have them available for other people to use
# that's whats so powerful about this concept - you can reuse code and then also make your own and make it available for others to reuse

# LIBRARIES: a collection of packages
# note: library, package, and module are sometimes used interchangeably, especially if there's only one module
# there are standard libraries that just come with python that you don't need to install
# for others, pip, a package manager, comes with python and there's a really easy command to get any package you want: pip install ***

# math
# provides useful functions like sqrt, pow, log, factorial, sin, cos, tan, round and useful constants like math.pi, e, inf
# examples of a bunch of those

# random
# provides functions to select/choose things basically randomly
# functions like randint, randrange, choice

# sys
# provides functions system related functions and attributes
# important one is argv

