'''
    Author: Nancy McCoy
    Description: PY4E Chapter 7: Files - Exercise 1; Write a program to read through a file and print the contents of the
    file (line by line) all in upper case.
'''

#Grabs the inputted file name
fname = input('Enter the file name:')
try:
    fhand = open(fname)
    #For every line in the file, prints as uppercase
    for line in fhand:
        print(line.upper())
#If the file isn't found, prints the exception
except:
    print("The file was not found. Try again.")



