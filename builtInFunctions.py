'''
this program demonstrates Python's many built in functions
'''
#A test string
testString = "I'M SHOUTING!!!!!!!!"
testString2 = "i'm not"
done = False
blankString = "               "
pDone = False
print(testString.isupper())
print(testString2.islower())

testString2 = testString2.upper()
print(testString2)
testString = testString.lower()
print(testString)

password = input("what is not your password? >")

#if a string is just letters
while pDone != True:
    if password.isalpha() == True:
        print("Your password is weaker than me")

    elif password.isspace() == True:
        print("Oi give us your password")
    else:
        print("nice password")
        pDone = True
#Checking numbers
while done != True:
    number = input('What is your phone number?  >')

    if number.isnumeric() != True:
        print('Please enter a number')

    elif len(number) != 11:
        print("That is not a valid UK telephone number.")

    else:
        print("ring ring")
        done = True

print("blankString is a blank string = ", blankString.isspace())
print(blankString.isspace())
