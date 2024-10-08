'''class Person:
    def __init__(self, firstname , lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print("my name is "+ self.firstname, "and my last name is  "+self.lastname)

    def details(self):
        print(self.firstname,self.lastname)

class Student(Person):
    pass

p1 = Person("rohan","jain")
p2 = Person("mohan","jain")
p1.printname()
p2.printname()
print(p1.firstname, p1.lastname)
print(p2.firstname,p2.lastname)'''
'''
x = Student("rohan","jain")
print(x.firstname)
x.printname()
x2 =Student("mohan","jain")
x2.printname()
x2.details()'''

class Car:
    def __init__(self, brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color
    def move (self):
        print("Drive")

class Boat(Car):
    def __init__(self, brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color

    def move(self):
        print("sail")
        print(self.brand)
class Plane(Boat):
    def __init__(self,brand,model,color):
        self.brand = brand
        self.color = color
        self.model = model
    def move(self):
        print("fly")

car1 = Car("tvs","red","new")
boat1 =Boat("ibiza", "i 20","blue")
#print(boat1.brand,boat1.model,boat1.color)
boat1.move()
plane1 =Plane("honda","23 ","white")

#for x in (car1,boat1, plane1):
  #  x.move()

  