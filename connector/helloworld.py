# -*- coding: utf-8 -*-


# print("hello world")
print("I am €")

"""
Exercise 7 - More printing
"""


#deea = "C"
#stefi = "h"
#mama = "e"
#dimi = "e"
#buni = "s"

#print(deea+stefi+mama+dimi+buni,)
#print("*"*95+"\n"+"#"*95)

#print("DIMI")

"""
Exercise 10

print("I am 6'2\" tall.")
print("\tI'm tabbed.")

while True:
    for i in ["/","-","|","\\","|"]:
        print('{0!s}'.format(i))
"""

"""
Exercise 11

print("How old are you?")
age = input('Provide your age: ')
try:
    val = int(age)
    print("you're {0} years old.".format(age))
except:
    print("Your value is not numeric.")
"""

"""
Exercise 13
"""
# from sys import argv

# script, first, second, third = argv

# print("The script is called: {}".format(script))
# print("Your first variable is: ", first)

"""
Exercise 14
"""

# from sys import argv
# script, user_name = argv
# prompt = ">>"

# print("Hi {0}, I'm the {1} script.".format(user_name, script))
# print("I'd like to ask you a few questions.")
# print("Do you like me {}".format(user_name))
# likes = raw_input(prompt)

# print("Where do you live {}".format(user_name))
# lives = raw_input(prompt)

# print("What kind of computer do you have?")
# computer = raw_input(prompt)

# print("""
# Alright, so you said '{1}' about liking me.
# You live in '{2}'. Not sure where that is.
# And you have a '{0}' computer. Nice.
# """.format(computer, likes, lives))


"""
Exercise 15
"""
# # import some needed modules
# # argv for example, helps reading user input from keyboard
# from sys import argv

# # argv[0] is scriptname, argv[1] is filename
# # we just happen to have named the values to mean same thing
# script, filename = argv

# # open the filename we pass as parameter when ran the sript
# txt = open(filename)

# # print the whole file read as a long string of characters
# # print is smart enough to correctly interpret \n new line
# print("Here's your file name: {}".format(filename))
# print(txt.read())

# txt.close()
# # input() method in pyton3 is same as raw_input() in python2
# print("Type the filename again:")
# file_again = input("> ")

# """
# print the new input file
# if not found an error will be displayed
# and script run will stop
# """
# txt_again = open(file_again)

# #print again the new input file
# print(txt_again.read())

# txt_again.close()


"""
Exercise 15
"""
from sys import argv

script, filename = argv

print("We are going to erase file: {}".format(filename))
print("If you don't want that, then hit CTRL-C.")
print("If you want that, then hit RETURN.")

input(">>")

print("Opening the file...")
target = open(filename,'w')

print("Truncating the file..Goodbye!")
target.truncate()

print("This is what the file contains now...")
target.close()
same_file = open(filename)
print(same_file.read())
print("That is basically...nothing")

print("Now I am going to write something to the file.")

line = []
target = open(filename,'w')

for i in range(1,4):
    line.append(input("line {}: ".format(i)))
    target.write(line[i-1])
    target.write("\n")

print("And finally, we close it.")
target.close()

print("What do you say we print out the final file?")
for i in open(filename):
    print(i)

"""
Exercise 17
"""


