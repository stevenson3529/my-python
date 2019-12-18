'''
creating a class of an animal and creating as a virtual pet
'''

maxWeight = 0
colours = ['black','white','grey','golden','brown','spotty','blue','green','pink']
sizes = ['1','2','3']
valid = ['1','2','3']

class Dog():
    def __init__(self,size,age,weight,name,colour,breed):
        #initialiasing attributes
        self.name = name
        self.size = size
        self.age = age
        self.weight = weight
        self.colour = colour
        self.breed = breed
        
    def obesity(self):
        if self.size == 1:
            maxWeight = 10
        elif self.size == 2:
            maxWeight = 20
        elif self.size == 3:
            maxWeight = 30
        if self.weight >= maxWeight:
            print("I am officialy obese")
        elif self.weight < maxWeight:
            print("I am a healthy weight")
        

    def feed(self, amount):
        #feeding the pet
        self.weight = self.weight + (amount / 10)
        print("my weight is now",self.weight)

    def walk(self,distance):
        self.weight = self.weight - (distance/10)
        print("good walk")
    
#when adding next method, use SELF!!!!!!!!!!
#add pet
#add mood
#add hunger
#add toilet time
#add commands
#drinking
#bed


#the user inputs the information about the dog
def createDog():
    dogName = input("Enter the dog's name  >")
    if dogName == "skip":
        dog1 = Dog(2,10,10,"Fred","golden","labrador")
        return
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
    #returns the attributes of the dog
    return dogSize, dogAge, dogWeight, dogName,dogColour,dogBreed
#stores the returned values in a tuple
retDog = createDog()
#creates the dog object
dog2 = Dog(retDog[0],retDog[1],retDog[2],retDog[3],retDog[4],retDog[5])
while True:
    print("virtual dog")
    print("------------------")
    print("Select an option:")
    print("1. Walk dog")
    print("2. Feed dog")
    print("3. Create a different dog")
    selected = False
    while selected != True:
        choice = input("Enter an option  >")
        if choice.isnumeric() == True:
            if choice in valid:
                choice = int(choice)
                selected = True
        else:
            print("Not a valid choice")
    if choice == 1:
        amount = input("How many kilometres to walk?  >")
        if amount.isnumeric() == True:
            amount = int(amount)
            dog2.walk(amount)
        else:
            print("Not a valid input")

    if choice == 2:
        amount = input("How much food to feed? (in kg)  >")
        if amount.isnumeric() == True:
            amount = int(amount)
            dog2.feed(amount)
        else:
            print("Not a valid input")
        
