'''
creating a class of an animal and creating as a virtual pet
'''

maxWeight = 0

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


dog1 = Dog(1,59,4,'sasha','black','collie')
dog1.feed(500)
dog1.obesity()
