'''
Program that calculates the total payroll in a company
'''
done = False
#a list of all the salaries
salaries = []

#Lets a user add a salary to the list
while done != True:
    add = input("Enter a salary to add to the list, or type no to cancel.  >")
    if add.isnumeric() == True:
        add = int(add)
        salaries.append(add)
    elif add.upper() == 'NO':
        done = True
    else:
        print("Enter a number, or type no to cancel.")

print("The total payroll is £", sum(salaries))
