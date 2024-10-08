class student:
    def __init__(self,name,java,python,dbms):
        self.name = name
        self.java = java
        self.python = python
        self.dbms = dbms


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0


        for varible in self.marks:

            sum += varible

            print(self.name,sum/3)

s1 = Student("pooja",[99, 98,97])
s1.get_avg()