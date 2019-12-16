'''
creating a class of an animal and creating as a virtual pet
'''

maxWeight = 0
colours = ['black','white','grey','golden','brown','spotty']
sizes = ['1','2','3']

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
        #obesity()


dogName = input("Enter the dog's name  >")
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
dog1 = Dog(dogSize,dogAge,dogWeight,dogName,dogColour,dogBreed)
dog1.feed(3)
dog1.obesity()


        
