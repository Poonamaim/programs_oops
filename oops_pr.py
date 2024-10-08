'''import math

class Circle:
    def __init__(self , radious):
        self.radious = radious


    def circle_area(self):
        return math.pi * self.radious**2

    def circle_area_of_perameter(self):
        return 2 * math. pi * self.radious

radious = float(input("enter the radious"))

circle = Circle(radious)
circle_area = circle.circle_area()
circle_perameter = circle.circle_area_of_perameter()
print(circle_area)
print(circle_perameter)'''

'''#Write a Python program to create a person class. Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.
from datetime import date
class Person:
    def __init__(self, name, country,date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth


    def calculate_person_age(self):
        today = date.today()
        age = today.year -self.date_of_birth.year

        if today< date(today.year,self.date_of_birth.month,self.date_of_birth.day):
            age = age-1
            return age
person1 = Person("rohan","india",date(2000, 7, 12))
person2 = Person("mohan","delhi",date(2003,8,13))

print("person1 data")
print("name" ,person1.name)
print("country", person1.country)
print("date_of_birth", person1.date_of_birth)
print(person1.calculate_person_age())'''

from datetime import date


# Define a class called Person to represent a person with a name, country, and date of birth
'''class Person:
    # Initialize the Person object with a name, country, and date of birth
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    # Calculate the age of the person based on their date of birth
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


# Example usage
# Create three Person objects with different attributes
person1 = Person("Ferdi Odilia", "France", date(1962, 7, 12))
person2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
person3 = Person("Elizaveta Tilman", "USA", date(2000, 1, 1))

# Access and print the attributes and calculated age for each person
print("Person 1:")
print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.date_of_birth)
print("Age:", person1.calculate_age())
'''

'''class Person:
    def __init__(self , name , roll, math, hindi, english):
        self.name = name
        self.roll = roll
        self.math = math
        self.hindi = hindi
        self.english = english

    def getmarks(self ):
        total_marks = self.math + self.english + self.hindi
        return total_marks

    def average_marks(self):
        total_marks = self.getmarks()
        vg = total_marks/3
        return vg

class Student(Person):
        def __init__(self, name, roll,math, hindi, english):
            super().__init__(name, roll,  math, hindi, english)
            self.java = 90
            self.python =100
            self.c =340
        def calculation(self):
            total = self.java + self.python + self.c
            return total
        def student_avg(self):
            total = self.calculation()
            avg =total /3
            return avg


math = int(input("enter the marks"))
english = int(input("enter the marks"))
hindi = int(input("enter the marks"))
person = Person("hi",3,math,english,hindi)
person1 = Person("reeta",2,76, 78, 90)
print(person.name)
print(person.roll)
person.getmarks()
print(person.getmarks())
person.average_marks()
print(person.average_marks())

person1.getmarks()
print(person1.getmarks())
person1.average_marks()
print(person1.average_marks())

student = Student("radha",23,90,80,89)
print(student.java)
print(student.python)
print(student.c)

student.calculation()
print( "student total marks is "+ str(student.calculation()))

student.student_avg()
print("student avg is " + str(student.student_avg()))'''

#polymorphism used
class Car:
    def __init__(self , color,type,brand,price):
        self.color = color
        self.type = type
        self.brand =brand
        self.price = price

    def move(self):
        print("automatic")

class Boat(Car):
    def __init__(self, color,type,brand,price):
        super().__init__(color, type,brand,price)
        self.advance = "new realease"
        self.avarage = 250

    def move(self):
        print("not a automatic")
car = Car("black","automatic ","cb1", 340000)
print(car.color)
print(car.brand)
car.move()






