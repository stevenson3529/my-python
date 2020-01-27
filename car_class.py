'''
A car program using classes
'''
class Car():
    def __init__(self,make,colour,year,odometer):
        self.make = make
        self.colour = colour
        self.year = year
        self.odometer = 0

    def describe_car(self):
        desc = "This car is a %s %s made in %s"%(self.colour,self.make,self.year)
        return desc

    def read_odo(self):
        #reads the odometer
        reading = "This car has done %s miles"%(self.odometer)
        return reading

    def update_odo(self,mileage):
        self.odometer = self.odometer + mileage
                   

car1 = Car("Fiat Panda","Red","2006","65000")
print(car1.describe_car())
car1.odometer = 90000
car1.update_odo(200)
print(car1.read_odo())
