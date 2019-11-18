'''
Introduction to classes and objects
'''

class Superhero():
    def fly(self):
        print("i can fly")
        
    def hotDog(self,num):
        print("I can eat", num , "hotdogs in a minute.")

    def cantFly(self):
        print("I am useless and have no flight abilities.")

superMan = Superhero()

superMan.fly()
superMan.hotDog(30)

notSuperMan = Superhero()

notSuperMan.cantFly()
notSuperMan.hotDog(3)
    
