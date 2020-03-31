'''
A module for user inputs, with validation.
'''
#A list of answers that mean yes or no:
yesses = ["y","Y","yes","Yes"]
nos = ["n","N","No","no"]

#q = question
#t = type (s = string, n = number, b = boolean)
def ask(q,t):
    if t == "s":
        print(q)
        userInput = input(">")
        return userInput
    elif t == "n":
        while True:
            print(q)
            userInput = input(">")
            if userInput.isnumeric() == True:
                return int(userInput)
            else:
                print("Not a valid input")
    elif t == "b":
        while True:
            print(q)
            userInput = input(">")
            if userInput in yesses:
                return True
            elif userInput in nos:
                return False
            else:
                print("Not a valid input")
    else:
        print("Sorry, an error has occured in the 'user_input' module.")


