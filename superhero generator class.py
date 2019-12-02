'''
An improved version of the Superhero Generator"
'''
import random
import time

def suspense(times):
    for t in range(times):
        time.sleep(0.8)
        print('.....')
    time.sleep(0.8)

def line():
    print('')
    
class Superhero():
    #initialising attributes of the hero
    def __init__(self):
        self.superName = superName
        self.superPower = myPower
        self.power = power
        self.speed = speed
        self.strength = strength
        self.intelligence = intelligence
        self.stamina = stamina
        self.courage = courage
        self.agility = agility

class Mutant(Superhero):
    def __init__(self):
        Superhero.__init__(self)
        print("A mutant superhero has been created!")
        #stronger, faster  and stupider
        self.speed =+ 10
        self.intelligence = self.intelligence - 5
        self.power =+ 5

class Robot(Superhero):
    def __init__(self):
        Superhero.__init__(self)
        print("A robot superhero has been created!")
        #cleverer and more corageous but slower and less agile
        self.speed =- 10
        self.intelliigence =+ 20
        self.courage =+ 20
        self.agility =- 10     
    
    
#Generating stats for a hero
power = random.randint(0,50)
speed = random.randint(0,50)
strength = random.randint(0,50)
intelligence = random.randint(0,50)
stamina = random.randint(0,50)
courage = random.randint(0,50)
agility = random.randint(0,50)

#choosing name and power
firstNames = ['Amazing', 'Speedy', 'Salty', 'Soapy', 'Crazy', 'Spicy', 'Alright', 'Hot', 'Cheesy','Plastic']
lastNames = ['Runner', 'Thinker', 'Cat Food', 'Pie', 'Carpet', 'Lasagne', 'Paper', 'Shelf','Table','Plastic']
superPowers = ['Super Speed', 'Levitation', 'X-Ray vision', 'Teleportation', 'Elasticity', 'Invisibility', 'Telekiness','Heightened sense of smell']
firstName = '0'
lastName = '0'
superName = random.choice(firstNames) + ' ' + random.choice(lastNames)
myPower = (random.choice(superPowers))

#Choose type of hero
def menu():
    chosen = False
    while chosen != True:
        print("choose type of hero:")
        print("1. Normal Superhero")
        print("2. Mutant superhero")
        print("3. Robot superhero")
        choice = input(">")
        if choice.isnumeric() == True:
            choice = int(choice)
            chosen = True
        else:
            print('not a valid choice')

    if choice == 1:
        #creating the superhero object
        hero = Superhero()
        #prints out the results
        print("Finding your superhero name.....")
        suspense(2)
        print("Your name is %s" %(hero.superName))
        print("Your main power is.....")
        suspense(3)
        print("Your main power is %s" %(hero.superPower))
        input("Press ENTER to continue.")
        print("Calculating your stats.....")
        suspense(4)
        print("Your stats are:")
        line()
        print("Power:          ",hero.power)
        print("Speed:          ",hero.speed)
        print("Strength:       ",hero.strength)
        print("Intelligence:   ",hero.intelligence)
        print("Stamina:        ",hero.stamina)
        print("Courage:        ",hero.courage)
        print("Agility:        ",hero.agility)
        line()
        input("Press ENTER to continue...")
    elif choice == 2:
        mutant = Mutant()
        print("Finding your superhero name.....")
        suspense(2)
        print("Your name is %s" %(mutant.superName))
        input("Press ENTER to continue...")
        print("Your main power is.....")
        suspense(3)
        print("Your main power is %s" %(mutant.superPower))
        input("Press ENTER to continue...")
        print("Calculating your stats.....")
        suspense(4)
        print("Your stats are:")
        line()
        print("Power:          ",mutant.power)
        print("Speed:          ",mutant.speed)
        print("Strength:       ",mutant.strength)
        print("Intelligence:   ",mutant.intelligence)
        print("Stamina:        ",mutant.stamina)
        print("Courage:        ",mutant.courage)
        print("Agility:        ",mutant.agility)
        line()
        input("Press ENTER to continue...")
    elif choice == 3:
        robot = Robot()
        print("Finding your superhero name.....")
        suspense(2)
        print("Your name is %s" %(robot.superName))
        input("Press ENTER to continue...")
        print("Your main power is.....")
        suspense(3)
        print("Your main power is %s" %(robot.superPower))
        input("Press ENTER to continue...")
        print("Calculating your stats.....")
        suspense(4)
        print("Your stats are:")
        line()
        print("Power:          ",robot.power)
        print("Speed:          ",robot.speed)
        print("Strength:       ",robot.strength)
        print("Intelligence:   ",robot.intelligence)
        print("Stamina:        ",robot.stamina)
        print("Courage:        ",robot.courage)
        print("Agility:        ",robot.agility)
        line()
        input("Press ENTER to continue...")
    else:
        print('not a valid choice')
while True:
    menu()

