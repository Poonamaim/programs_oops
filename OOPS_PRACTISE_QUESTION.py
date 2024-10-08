# class 1 example
'''class Person:
  def __init__(self, fname, lname,math):
    self.firstname = fname
    self.lastname = lname
    self.math = math

  def printname(self):
    print(self.firstname, self.lastname,self.math)

class Student(Person):
  def __init__(self, fname, lname,math):
    super().__init__(fname, lname,math)
    self.graduationyear = 2023
    self.age =20
    self.marks = 44
    self.math =45

x = Student("Mike", "Olsen",56)
x1 = Person("java","python",67)
x1.printname()
x.printname()
print(x.graduationyear)
print(x.math)
print(x.marks)
'''
#2 . class example
'''class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
p2 =Person("mohan",34)
p3 =Person("sohan",43)

print(p1.name)
print(p2.age)
print(p3.name)
'''
# ex3
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
    self.marks = 2024

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x1 =Person("mike","selon")
x1.printname()
x.welcome()
x2 =Student("rohan","sohan",89)
x2.printname()

# 4
class Calculator:



  def add(self, x,y):
    return x+y

  def mul(self, x,y):
    return x*y

  def div(self ,x,y):
    return x/y

  def module(self, x,y):
    return x%y
'''x = float(input("enter the value"))
y = float(input("enter the y value"))'''
calculator = Calculator()
x = calculator.add(3,5)
print(x)

mul = calculator.mul(56,8)
print(mul)



