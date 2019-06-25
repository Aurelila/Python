''' Author: Nancy McCoy
    Description: Asks user for their name and age and tells them how old they would be in 100 years.
'''

name = input("What is your name?")
age = int(input("How old are you?"))
year = int(age) + 100
output = print("You will be " + '' + str(year) + " in 100 years " + name)
