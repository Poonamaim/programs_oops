class Student:
    name = "name"# class attr

    def __init__(self,roll,english,sci,math,marks):
        self.roll =roll   # obj attr > class attr
        self.english =english
        self.sci = sci
        self.math = math
        self.marks =marks
        print(" student")

obj =Student(1,90,80,97,100)

print(obj.roll,obj.english , obj.sci , obj.math,obj.marks)
print(obj.math)

obj2 = Student(2,80,90,70,100)
print(obj2.roll,obj2.english,obj2.sci,obj2.math,obj2.marks)


