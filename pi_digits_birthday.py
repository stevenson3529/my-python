'''
A program that finds if a user's birthday appears in the first million digits of pi.
Using the 'ddmmyy' format
'''
import user_input

filename = 'assets/pi_million_digits.txt'

with open(filename) as pi_digits:
    lines = pi_digits.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

usersBDay = user_input.ask("Please enter your birthday in the form ddmmyy","s")

if usersBDay in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Sorry, your birthday does not apepar to be in the first million digts of pi.")
