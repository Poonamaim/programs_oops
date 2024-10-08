'''class Person:
  def __init__(self, fname, lname,math):
    self.firstname = fname
    self.lastname = lname
    self.math = math

  def printname(self):
    print(self.firstname, self.lastname,self.math)

class Student(Person):
  def __init__(self, fname, lname,math,sci):
    super().__init__(fname, lname,math)

    self.graduationyear = 3458
    self.age =20
    self.marks = 44
    #self.math =45
    self.sci = sci

x = Student("Mike", "Olsen",56,45)
x1 = Person("java","python",67)
#x1.printname()
x.printname()
print(x.sci)



class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year, marks, roll):
        super().__init__(fname, lname)
        self.graduationyear = year
        self.marks = marks
        self.roll = roll
        self.city = "delhi"


x = Student("Mike", "Olsen", 2019, 90, 12)
print(x.graduationyear)
print(x.city)'''

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

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

#x = Student("Mike", "Olsen", 2024)
#x1 =Person("mike","selon")
#x1.printname()
#x.welcome()
x2 =Student("rohan","sohan",89)
x2.printname()



#Write a Java program to create a class called "Person" with a name and age attribute.
# Create two instances of the "Person" class, set their attributes using the constructor, and print their name and age.
'''class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age


    def getAge(self):
        return self.age
    def getname(self):
        return self.name

person = Person("mohan",23)
c =person.getAge()
c1 =person.getname()
print(c)
print(c1)'''

#2. Write a Java program to create a class called "Dog" with a name and breed attribute.
# Create two instances of the "Dog" class, set their attributes using the constructor and modify
# the attributes using the setter methods and print the updated values.

'''class Dog:
    def __init__(self ,name,breed):
        self.name = name
        self.breed = breed

    def setname(self):
        return self.name

    def getbreed(self):
        return self.breed

dog = Dog("tommy","white")
print(dog.setname())
print(dog.getbreed())'''



'''#class called "Rectangle" with width and height attributes.
#Calculate the area and perimeter of the rectangle.
class Rectangle:
    def __init__(self, width,heigth):
        self.width = width
        self.heigth =heigth

    def area(self):
        area = self.width * self.heigth
        return area

    def perameter(self):
        perameter = 2 * (self.width * self.heigth)
        return perameter

rectangle = Rectangle(23,45)
print(rectangle.area())
print(rectangle.perameter())
'''

#Write a Java program to create a class called "Circle" with a radius attribute.
# You can access and modify this attribute. Calculate the area and circumference of the circle.
'''import math
class Circle:
    def __init__(self , radious):
        self.radious = radious

    def area_of_circle(self):
        circle_area = math.pi * self.radious * self.radious
        return circle_area
    def circumference(self):
        circumference = 2 * math.pi * self.radious
        return circumference

circle = Circle(3)
print(circle.area_of_circle())
print(circle.circumference())'''

#Write a Java program to create a class called "Book" with attributes for title, author, and ISBN,
# and methods to add and remove books from a collection.
class Book:
    def __init__(self, title,author,ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def add_book(self):
        books = {"math", "english", "hindi"}

        books.add("science")
        books.add("java")
        books.add("python")

        return books

    def remove_books(self):
      books = self.add_book()
      removes = books.remove("java")
      return removes

book = Book("life_rule","rovin","abc")
print(book.title)
print(book.author)
print(book.add_book())



print(book.remove_books)








