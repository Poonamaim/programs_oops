class Student1:

    def __init__(self,roll,english,sci,math,marks):
        self.roll =roll   # obj attr > class attr
        self.english =english
        self.sci = sci
        self.math = math
        self.marks =marks
        print(" student")

    def WELCOME(self):
        print("hello",self.roll,self.math,self.marks,self.sci)
    def get_marks(self):
        return self.sci

s1 = Student1(1,100,70,90,80)
#print(s1.roll,s1.english,s1.math)

s1.WELCOME()
print(s1.get_marks())
print(s1.get_marks())