'''
An improved version of the Superhero Generator"
'''
import random

class Superhero():
    #initialising attributes of the hero
    def __init__(self):
        self.superName = ' '
        self.superPower = ' '
        self.power = power
        self.speed = speed
        self.strength = strength
        self.intelligence = intelligence
        self.stamina = stamina
        self.courage = courage
        self.agility = agility

#Generating stats for a hero
power = random.randint(0,10)
speed = random.randint(0,10)
strength = random.randint(0,10)
intelligence = random.randint(0,10)
stamina = random.randint(0,10)
courage = random.randint(0,10)
agility = random.randint(0,10)

#Creating a hero object
hero = Superhero()

#entering name
print("Enter your super name")
hero.superName = input ("> ")

#print out the results
print("Your name is %s" %(hero.superName))
print("Your stats are:")
print(" ")
print("Power:          ",hero.power)
print("Speed:          ",hero.speed)
print("Strength:       ",hero.strength)
print("Intelligence:   ",hero.intelligence)
print("Stamina:        ",hero.stamina)
print("Courage:        ",hero.courage)
print("Agility:        ",hero.agility)

