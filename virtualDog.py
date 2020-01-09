'''
creating a class of an animal and creating as a virtual pet
'''

import time as t

maxWeight = 0
colours = ['black','white','grey','golden','brown','spotty','blue','green','pink']
sizes = ['1','2','3']
valid = ['1','2','3','4','5']
global dog2

def l():
    #adds a blank line
    print('')
    
class Dog():
    def __init__(self,size,age,weight,name,colour,breed):
        #initialiasing attributes
        self.name = name
        self.size = size
        self.age = age
        self.weight = weight
        self.colour = colour
        self.breed = breed
        self.relationship = 50
        self.thirst = 0
        

    def obesity(self):
        if self.size == 1:
            maxWeight = 10
            minWeight = 1.5
        elif self.size == 2:
            maxWeight = 20
            minWeight = 5
        elif self.size == 3:
            maxWeight = 30
            minWeight = 12.5
        if self.weight >= maxWeight:
            print("I am officialy obese")
        elif self.weight < maxWeight:
            print("I am a healthy weight")
        if self.weight < minWeight:
            self.weight = minWeight
        

    def feed(self, amount):
        #feeding the pet
        weightGain = amount / 100
        self.weight = self.weight + weightGain
        self.thirst += 10
        dog2.isThirsty()
        print("my weight increased by",weightGain,"and my weight is now",self.weight)
        dog2.obesity()
        input("Press ENTER to continue...")

    def walk(self,distance):
        print("Walking dog...")
        t.sleep(distance / 2)
        print("good walk")
        weightLoss = distance /10
        self.weight = self.weight - weightLoss
        self.thirst += distance * 2
        dog2.isThirsty()
        obesity()
        print("I lost",weightLoss,"kilograms and I now weigh",self.weight,"kg.")
        input("Press ENTER to continue...")

    def info(self):
        print("I am "+self.name+", a",self.age,"year old",self.breed,"who weighs",self.weight,"kilograms.")
        self.thirst += 1
        dog2.isThirsty()
        print("Our relationship is "+str(self.relationship)+"%")
        dog2.obesity()
        input("Press ENTER to continue...")        

    def pet(self,much):
        print("petting...")
        t.sleep(much)
        more = self.relationship + much
        self.relationship += more
        self.thirst += 2
        dog2.isThirsty()
        print("our relationship improved by " + str(much) + "% and is now " + str(self.relationship) + "%")
        input("Press ENTER to continue...")

    def drink(self):
        print("Drinking...")
        t.sleep(self.thirst / 10)
        self.thirst = 0
        print("I am no longer thirsty.")
        input("Press ENTER to continue...")
        
        
    def isThirsty(self):
        #checks if the dog is thirsty
        if self.thirst < 70:
            print("I am not thirsty")
        elif self.thirst >= 70 and self.thirst < 90:
            print("I am rather thirsty...")
        elif self.thirst >= 90 and self.thirst < 100:
            print("I am very thirsty!")
        elif self.thirst >= 100:
            print("I AM EXTREMELY THIRSTY!!!")

           

#when adding next method, use SELF!!!!!!!!!!
#add mood
#add hunger
#add toilet time
#add commands

#the user inputs the information about the dog
def createDog():
    dogName = input("Enter the dog's name  >")
    dogName = dogName.capitalize()
    if dogName == "Skip":
        dogName = 'Fred'
        dogAge = 10
        dogWeight = 15
        dogColour = 'black'
        dogSize = 2
        dogBreed = 'pitbull'
        return dogSize, dogAge, dogWeight, dogName,dogColour,dogBreed
    ageDone = False
    weightDone = False
    colourDone = False
    sizeDone = False
    while ageDone != True:
        input1 = input("Enter the dogs age  >")
        if input1.isnumeric() == True:
            dogAge = int(input1)
            ageDone = True
        else:
            print("Not a valid input")
    while weightDone != True:
        input2 = input("Enter the dogs weight (in kg)  >")
        if input2.isnumeric() == True:
            dogWeight = int(input2)
            weightDone = True
        else:
            print("Not a valid input")
    while colourDone != True:
        input3 = input("Enter the dogs colour  >")
        if input3 in colours:
            dogColour = input3
            colourDone = True
        else:
            print("Not a valid input")
    while sizeDone != True:
        input4 = input("Enter the dogs size(1 for small, 2 for medium, 3 for large)  >")
        if input4.isnumeric() == True and input4 in sizes:
            dogSize = int(input4)
            sizeDone = True
        else:
            print("Not a valid input")
    dogBreed = input("enter the dog's breed  >")
    #returns the information of the dog
    return dogSize, dogAge, dogWeight, dogName,dogColour,dogBreed

#stores the returned values in a tuple
retDog = createDog()
    
#creates the dog object
dog2 = Dog(retDog[0],retDog[1],retDog[2],retDog[3],retDog[4],retDog[5])

def menu():
    l()
    print("Virtual dog main menu")
    print("------------------")
    print("Select an option:")
    print("1. Walk dog")
    print("2. Feed dog")
    print("3. Water dog")
    print("4. Information about your dog")
    print("5. Spend time with your dog")
    print("6. Quit")
    selected = False
    while selected != True:
        choice = input("Enter an option  >")
        if choice.isnumeric() == True:
            if choice in valid:
                choice = int(choice)
                selected = True
                l()
        else:
            print("Not a valid choice")
    if choice == 1:
        amount = input("How many kilometres to walk?  >")
        if amount.isnumeric() == True:
            amount = int(amount)
            dog2.walk(amount)
        else:
            print("Not a valid input")

    elif choice == 2:
        amount = input("How much food to feed? (in grams)  >")
        if amount.isnumeric() == True:
            amount = int(amount)
            if amount < 2000:
                dog2.feed(amount)
            else:
                print("Too much food!")
        else:
            print("Not a valid input")
    elif choice == 3:
        dog2.drink()
    elif choice == 4:
        dog2.info()
    elif choice == 5:
        amount = input("How much time to spend with your dog? (in seconds)  >")
        if amount.isnumeric() == True:
            amount = int(amount)
            dog2.pet(amount)
        else:
            print("Not a valid input")

    elif choice == 6:
        bad = True
        return bad

while True:
    bad = menu()
    if bad == True:
        print("goodbye")
        break
