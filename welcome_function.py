''' Author: Nancy McCoy
    Description: The function belows asks the user their name which is assigned to the variable "name". I then created three variables "age, young, older".
    I then take the user's inputted age from the variable "age" and add and minus 10 years to it with "young and older". The print statements print the user's
    inputted age with the new variables "young and older" showcasing how young they were 10 years ago and how old they would be 10 years from now.
'''

def welcome_function():
    name = input("What is your name?")
    print("Welcome to my function" + name + "!")
    age = int(input("How old are you?"))
    young = age - 10
    older = age + 10
    print("You were" + ' ' + str(young) + ' ' + "ten years ago")
    print("You are going to be" + ' ' + str(older) + ' ' + " ten years from now")

welcome_function()