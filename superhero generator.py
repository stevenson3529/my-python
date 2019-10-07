'''
A super hero generator with stats, name and super powers
'''
import time, random

#Variables
start = 0
firstNames = ['Amazing', 'Speedy', 'Salty', 'Soapy', 'Crazy', 'Spicy', 'Alright', 'Hot', 'Cheesy','Plastic']
lastNames = ['Runner', 'Thinker', 'Cat Food', 'Pie', 'Carpet', 'Lasagne', 'Paper', 'Shelf','Table','Plastic']
superPowers = ['Super Speed', 'Levitation', 'X-Ray vision', 'Teleportation', 'Elasticity', 'Invisibility', 'Telekiness','Heightened sense of smell']
firstName = '0'
lastName = '0'
fullName = random.choice(firstNames) + ' ' + random.choice(lastNames)
power = (random.choice(superPowers))
keep = 0

#Stats
Power = random.randint(0,10)
Speed = random.randint(0,10)
Strength = random.randint(0,10)
Intelligence = random.randint(0,10)
Stamina = random.randint(0,10)
Courage = random.randint(0,10)
Agility = random.randint(0
                         ,10)
Total = Power + Speed + Strength + Intelligence + Stamina + Courage + Agility

def suspense(times):
    for t in range(0,times):
        time.sleep(0.8)
        print('.....')
    time.sleep(0.8)

answer = input('Would you like to start the ProSuperhero generator? (Y/N) >')
answer = answer.upper()
'''
if answer == 'Y':
print('Phenomenal. Let\'s get started!')
    print('Your superhero name is: ' + fullName)


elif answer == 'N':
    print('Goodbye')
else:
    print('Please enter Y or N.')
'''
while answer != 'Y':
    print('Choose Y to continue or Control-C to exit.')
    answer = input('Would you like to start the ProSuperhero generator? (Y/N) >')
    answer = answer.upper()

print('Phenomenal. Let\'s get started!')
print ('Finding your superhero name........')
suspense(3)

    
print('Your superhero name is: ' + fullName)
keep = input('Press ENTER to continue...')


print('Next, we\'ll find your superpower!')
time.sleep(1)
print('Detecting superpower...')
suspense(4)
print(power)
keep = input("Press ENTER to continue...")

print("Finally, lets check your stats.")
time.sleep(1)
print('Your stats are as follows...')
time.sleep(1)
print('Power: ' + str(Power) + '/10')
time.sleep(1)
print('Speed: ' + str(Speed) + '/10')
time.sleep(1)
print('Strength: ' + str(Strength) + '/10')
time.sleep(1)
print('Intelligence: ' + str(Intelligence) + '/10')
time.sleep(1)
print('Stamina: ' + str(Stamina) + '/10')
time.sleep(1)
print('Courage: ' + str(Courage) + '/10')
time.sleep(1)
print('Agility: ' + str(Agility) + '/10')
print('Your overall score is: ' + str(Total) + '/70!')
time.sleep(1)
print('Well done ' + fullName + '! Now go off and use your ' + power + ' for good!')
time.sleep(5)
print('Goodbye')

    

