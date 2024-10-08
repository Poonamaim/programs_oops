'''class person:
    __name = "pooja"

    def __hello(self):# this class will genrate error because this class attributes and method is private
        print("hello person")
p1 = person()
print(p1.__hello())'''


class person:
    name = "pooja"

    def hello(self):
        print("hello person")
p1 = person()
print(p1.hello())