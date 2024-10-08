'''class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
'''
'''person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
print(person1)

def cube(y):
    return y*y*y

lambda_cube = lambda y: y*y*y
print("Using function defined with `def` keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))'''

'''def square(x):
    return x*x
lambda_square = lambda x :x*x
print(square(3))

def cube(f):
    return f*f*f
lambda_cube = lambda f : f*f*f
print(lambda_cube(45))

a =  lambda x : x+ 25
print(a(2))
b = lambda y : y+ cube(y)
print(b(4))

student_data= [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(student_data)
student_data.sort(key=lambda x: x[1])
print("\nSorting the List of Tuples:")
print(student_data)
'''
'''student_data1 = [{'name': 'rohan', 'rollno': 216, 'subject': '["math","science","english"]','marks' :'[90,80,80]','total':2523},
                 {'name': 'seeta', 'rollno': '2', 'subject': '["math","science","english"]','marks':' [90,95,70]', 'total': 525}]
print(student_data1)
student_data2=sorted(student_data1,key=lambda x: x['total'])

max_value = max(student_data2, key=lambda x : x['total'])
'''
#import re

'''txt = input("enter the sentence")

x = re.findall("[a-f]", txt)
print(x)'''
'''import re
txt = input("enter the sentence")
x = re.findall("^hello",txt)
if x:
    print("yes hello Presented/n")
else:
    print("no match")
'''
import re

txt = input("enter the sentence")
x = re.findall(" hello$", txt)
if x:
  print("Yes, the string end with 'hello'")
else:
  print("No match")

