'''
A restaurant application involving classes.
'''

class User():
    def __init__(self,name,adress,phone):
        self.name = name
        self.adress = adress
        self.phone = phone

    def describe_user(self):
        print("%s lives at %s and their number is %s"%(self.name,self.adress,self.phone))

    def greet_user(self):
        print("Welcome back, %s" %(self.name))
        
class Restaurant():
    #A class of a restaurant
    def __init__(self,cuisine,name):
        self.name = name
        self.cuisine = cuisine
        self.open = False

    def describe_restaurant(self):
        #prints info about the restaurant
        print("This restaurant is called %s and serves %s food."%(self.name,self.cuisine))

    def open_restaurant(self):
        #opens the restaurant and prints confirmation
        self.open = True
        print("%s is open" %(self.name))

    def food_menu(self):
        if self.cuisine == "English":
            foods = ['Fish','Chips','Bacon','Egg','Bread','Heinz Beans']
        elif self.cuisine == 'Indian':
            foods = ['Naan bread','Poppadoms','Chicken tikka masala','chicken ceylon (!)',
                     'chicken korma','rice','Butter chicken', 'Vindaloo (!!)']
        elif self.cuisine == 'Chinese':
            foods = ['Sweet and sour chicken balls','Noodles','Pork chops']

    def user_menu(self):
        choices = [1,2,3,4]
        print("Main menu")
        print("---------")
        print("1. Desription of this restaurant")
        print("2. Show the food menu")
        print("3. Open the restaurant")
        print("4. Enter the restaurant")
        done = False
        while done != True:
        

restaurant1 = Restaurant("English","Brian's chip shop")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2 = Restaurant("Indian","Yatton Tandoori")
restaurant2.describe_restaurant()
restaurant3 = Restaurant("Chinese","China Star")
restaurant3.describe_restaurant()      
user1 = User("Antonio","49 High Street","07421 586831")
user1.describe_user()
user1.greet_user()
