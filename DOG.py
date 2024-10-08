'''class Dog:
    def __init__(self, color , name, eat):
        self.color = color
        self.name = name
        self.eat = eat

    def showattribute(self):

        list= self.color,self.eat,self.name
        return list

dog = Dog("black","tiger","bread")
print(dog.showattribute())'''

#Task: Create a Book class that has the following properties:

#title
#author
#year

'''class Book:
    def __init__(self, title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def titlename(self):
        return self.title


    def authorname(self):
        return self.author

    def yearname(self):
        return self.year

book = Book('life lesson',"rovin sharma", "2024")

print(book.titlename())
print(book.yearname())
print(book.authorname())'''
'''class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def description(self):
        return f"{self.title} by {self.author}, published in {self.year}"

book1 = Book("1984", "George Orwell", 1949)
print(book1.description())  '''


class Animal:
    def spkeak(self):
        return "sound of animal"



class Dog(Animal):
    def spkeak(self):
        return "Whoof Woof"

class Cat(Animal):
    def speak(self):
        return "meow"


if __name__ == "__main__":
    my_dog = Dog ()
    my_cat = Cat ()
print (my_dog.spkeak ())
print (my_cat.spkeak ())



