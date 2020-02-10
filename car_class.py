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
    def __init__(self,maxCharge):
        self.maxCharge = maxCharge
        self.chargeLevel = 0

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
        self.batt = Battery(2300)
                 

#car1 = Car("Fiat Panda","Red","2006","65000")
#print(car1.describe_car())
#car1.odometer = 90000
#car1.drive()
#print(car1.read_odo())
car2 = Electric_Car("Tesla Model S","Black","2019","10000")
print(car2.describe_car())
print(car2.read_odo())
car2.batt.charge()
