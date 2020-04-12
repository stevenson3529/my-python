'''
A program that prints the digits of pi
'''

filename = 'assets/pi_digits.txt'
#opens the file
with open(filename) as digits_file:
    '''
    digits = digits_file.read()
    print(digits)
    for line in digits_file:
        print(line.rstrip())
    '''
    lines = digits_file.readlines()

#loops through all the lines and prints them
'''
for line in lines:
    print(line.rstrip())
'''

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:56])
print('----------------')
print(len(pi_string),"characters in file")
