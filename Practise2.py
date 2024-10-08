class student:
    def __init__(self,name,java,python,dbms):
        self.name = name
        self.java = java
        self.python = python
        self.dbms = dbms

    def getTotalMarks(self):

        totalMarks = self.java + self.python + self.dbms
        return totalMarks


    def getPercentage(self):
        totalMarks = self.getTotalMarks()
        percentage = totalMarks / 3
        return percentage



stdobj = student(1,80,90,85)

stdobj2 = student(2,80,90,80)
stdobj3 = student(4,90,80,95)
stdobj4 = student(5,90,80,85)

stdobj = student(stdobj.name,stdobj2.java,stdobj3.python,stdobj4.dbms)



print("Total Marks: " + str(stdobj.getTotalMarks()))

print("Total Percentage: " + str(stdobj.getPercentage()))


print("Total Marks: " + str(stdobj2.getTotalMarks()))

print("Total Percentage: " + str(stdobj2.getPercentage()))


print("Total Marks: " + str(stdobj3.getTotalMarks()))

print("Total Percentage: " + str(stdobj3.getPercentage()))

print("Total Marks: " + str(stdobj4.getTotalMarks()))

print("Total Percentage: " + str(stdobj4.getPercentage()))
exit()