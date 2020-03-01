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
        self.odometer = 0
        self.fuel = 100

    def describe_car(self):
        #returns a description of the car
        desc = "This car is a %s %s made in %s."%(self.colour,self.make,self.year)
        return desc

    def read_odo(self):
        #reads the odometer
        reading = "This car has done %s miles"%(self.odometer)
        return reading

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
        else:
            print("You don't have enough fuel left!")

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
                 
def createCar(carType):
    initMake = input("What make/model is the car?  >")
    initColour = input("What colour is the car?  >")
    initYear
    if carType == "p":
        car1 = Car(initMake,initColour,initYear,initOdo)
    elif carType == "e":
        car1 = Electric_Car(initMake,initColour,initYear,initOdo)

def chooseType():
    initType = input("Electric or petrol vehicle?  >")
    if initType.upper() == "PETROL" or initType.upper == "DIESEL":
        createPetrolCar("p")
    elif initType.upper() == "ELECTRIC":
        createElectricCar("e")
    else:
        print("Not a valid input!")
        chooseType()
    

chooseType()

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
