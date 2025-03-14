# Hashem Barudi
# pseudocode:
# start
# display prompts for the user to input name and age as strings
#  and store them in name and age as variables
# then display the users name and age on the first output line
# the second line display Hello, World!
# stop
# for real start:
print("After each prompt, when done typing press enter to continue.")
# this is to make sure the user hits the enter key when typing their responses
name = input("Type your name: ")
age = input("Type your age: ")
# name and age collected and displayed below along with the closing message
print("My name is {} and I am {} years old.".format(name, age))
print("Hello, World!")
# closing the program by making the user hit enter
close_the_program = input("Close the program by pressing the enter key")
# cleanup
del close_the_program
del name
del age
# exit
exit()
# very simple first task.
# I want to make a modernized version of each task,
# simply check my modernized file and see its code.
# But will do this later.
#
# Pseudocode:
# 1. Ask the user for their name
# 2. Print the user's name
# 3. Ask the user for their age
# 4. Print the user's age
# 5. Print "Hello World!"
# Ask the user for their name.
# name = input("Please enter your name: ")
# Print the user's name
# print("Your name is " + name)
# Ask the user for their age.
# age = input("Please enter your age: ")
# Print the user's age
# print("Your age is " + age)
# Print "Hello World!"
# print("Hello World!")