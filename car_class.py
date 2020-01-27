'''
A car program using classes
'''
import time as t

locations = ['Edinburgh','Glasgow','Greenock','Carlisle','Berwick-upon-Tweed','Newcastle','York','Manchester','Birmingham','Hull','London','Norwich','King\'s Lynn','Southend-on-Sea','Southampton','Exeter','Cardiff','Bristol','Swansea','Fishguard','Llandudno']

class Car():
    def __init__(self,make,colour,year,odometer,fuelType):
        self.make = make
        self.colour = colour
        self.year = year
        self.odometer = 0
        self.fuelType = fuelType

    def describe_car(self):
        #returns a description of the car
        desc = "This car is a %s %s made in %s. It runs on %s power."%(self.colour,self.make,self.year,self.fuel)
        return desc

    def read_odo(self):
        #reads the odometer
        reading = "This car has done %s miles"%(self.odometer)
        return reading

    def update_odo(self,mileage):
        self.odometer += mileage

    def drive(self):
        originDone = False
        while originDone != True:
            print("Where from?")
            origin = input(">")
            if origin in locations:
                originDone = True
            else:
                print("no")
        destDone = False
        while destDone != True:
            print("Where to?")
            dest = input(">")
            if dest in locations:
                destDone = True
            else:
                print("no")
        print("How many miles to drive?")
        toDrive = int(input(">"))
        print("Driving...")
        t.sleep(toDrive / 10)
        self.update_odo(toDrive)

class Battery():
    def __init__(self,maxCharge,chargeLevel):
        self.maxCharge = maxCharge
        self.chargeLevel = chargeLevel

    def charge(self):
        timeCharge = 100 - chargeLevel
        timeCharge = timeCharge / 10
        print("charging battery...")
        t.sleep(timeCharge)
        chargeLevel = 100
        print("Charged!")                   

car1 = Car("Fiat Panda","Red","2006","65000","Petrol")
print(car1.describe_car())
car1.odometer = 90000
car1.drive()
print(car1.read_odo())
