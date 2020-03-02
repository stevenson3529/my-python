'''
A car program using classes
'''
import time as t

locations = ['Edinburgh','Glasgow','Greenock','Carlisle','Berwick-upon-Tweed','Newcastle','York','Manchester','Birmingham','Hull','London','Norwich','King\'s Lynn','Southend-on-Sea','Southampton','Exeter','Cardiff','Bristol','Swansea','Fishguard','Llandudno']

class Car():
    def __init__(self,make,colour,year,odometer):
        self.make = make
        self.colour = colour
        self.year = year
        self.odometer = odometer
        self.fuel = 100

    def describe_car(self):
        #returns a description of the car
        print("This car is a %s %s made in %s."%(self.colour,self.make,self.year))
        input("Press ENTER to continue...")
        
    def read_odo(self):
        #reads the odometer
        print("This car has done %s miles"%(self.odometer))
        input("Press ENTER to continue...")

    def update_odo(self,mileage):
        #adds the recent mileage to the odometer
        self.odometer += mileage

    def drive(self):
        #Take the car for a drive
        print("How many miles to drive?")
        toDrive = int(input(">"))
        if self.fuel >= (toDrive / 10) :
            print("Driving...")
            t.sleep(toDrive / 10)
            self.fuel -= toDrive / 10
            self.update_odo(toDrive)
            print("Driven %s miles."%(toDrive))
            input("Press ENTER to continue...")
        else:
            print("You don't have enough fuel left!")
            input("Press ENTER to continue...")

    def fill_car(self):
        '''
        Works out how much fuel the car needs.
        Example:
            fuel = 20%
            100 - 20 = 80
            80 / 5 = 16 seconds
        The car will take 16 seconds to fill up.
        '''
        timeFill = 100 - self.fuel
        timeFill = timeFill /5
        print("Filling car with petrol...")
        t.sleep(timeFill)
        self.fuel = 100
        print("A full tank is a happy tank.")
        print("Car filled with petrol.")
        input("Press ENTER to continue...")

class Battery():
    def __init__(self,maxCharge,chargeLevel):
        self.maxCharge = maxCharge
        self.chargeLevel = chargeLevel
        
    def charge(self):
        #Charging the battery
        timeCharge = 100 - self.chargeLevel
        timeCharge = timeCharge / 10
        print("charging battery...")
        t.sleep(timeCharge)
        self.chargeLevel = 100
        print("Charged!")  

class Electric_Car(Car):
    #creating a sub-class of the Car class
    def __init__(self,make,colour,year,odometer):
        #connects to the parent Car class
        super().__init__(make,colour,year,odometer)
        self.batt = Battery(2300,0)
        self.fuel = 0

    def fill_car(self):
        self.batt.charge()
                 
def menu():
    print("Car menu")
    print("--------------")
    print("Select an option:")
    print()
    print("1. Drive car")
    print("2. View information about car")
    print("3. Read odometer")
    print("4. Fill up car")
    print("5. Quit")
    print()
    choice = input(">")
    if choice.isnumeric() == True:
        choice = int(choice)
        if choice ==  1:
            car1.drive()
        elif choice == 2:
            car1.describe_car()
        elif choice == 3:
            car1.read_odo()
        elif choice == 4:
            car1.fill_car()
        elif choice == 5:
            return True
        else:
            print("Not a valid input.")
    else:
        print("Not a valid input.")



#Choosing the type of car
initType = input("Electric or petrol vehicle?  >")
if initType.upper() == "PETROL" or initType.upper() == "DIESEL":
    carType = "p"
elif initType.upper() == "ELECTRIC":
    carType = "e"
else:
    print("Not a valid input!")
    chooseType()

#Creating the car
initMake = input("What make/model is the car?  >")
if initMake == "skip":
    car1 = Car("Honda Civic","grey","2008","90000")
else:
    initColour = input("What colour is the car?  >")
    initYear = input("What year was the car made?  >")
    initOdo = input("How many miles has the car done?  >")
    if carType == "p":
        car1 = Car(initMake,initColour,initYear,initOdo)
    elif carType == "e":
        car1 = Electric_Car(initMake,initColour,initYear,initOdo)

while True:
    kill = menu()
    if kill == True:
        print("Goodbye")
        break

'''
car1 = Car("Fiat Panda","Red","2006","65000")
print(car1.describe_car())
car1.odometer = 90000
#car1.drive()
print(car1.read_odo())
car1.fuel = 10
#car1.fill_car()
car2 = Electric_Car("Tesla Model S","Black","2019","10000")
print(car2.describe_car())
print(car2.read_odo())
car2.fill_car()
'''
