import xlsxwriter
class Student:
    def __init__(self, roll,eng,sci, math):
        self.roll = roll
        self.eng = eng
        self.sci = sci
        self.math = math

    def displayMarks(self):
        print("english: " + str((self.eng)))
        print("Science: " + str((self.sci)))
        print("math: " + str((self.math)))


    def getTotalMarks(self):
        totalMarks = self.eng + self.sci + self.math
        return totalMarks

    def getPercentage(self):
        totalMarks = self.getTotalMarks()
        percentage = totalMarks / 3
        return percentage

    def createExcelofMarks(self):
        totalMarks = self.getTotalMarks()
        percentage = self.getPercentage()

        workbook = xlsxwriter.Workbook('studentMarks.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Roll Number')
        worksheet.write('B1', 'English')
        worksheet.write('C1', 'Science')
        worksheet.write('D1', 'Math')
        worksheet.write('E1', 'Total Marks')
        worksheet.write('F1', 'Percentage')

        worksheet.write('A2', self.roll)
        worksheet.write('B2', self.eng)
        worksheet.write('C2', self.sci)
        worksheet.write('D2', self.math)
        worksheet.write('E2', totalMarks)
        worksheet.write('F2', percentage)
        workbook.close()
'''
roll = int(input("Enter roll number"))
eng = int(input("Enter Eng number"))
sci = int(input("Enter Sci number"))
math = int(input("Enter Math number"))'''


stdobj=Student(1,90,80,70)
stdobj1=Student(2,90,80,70)
stdobj2=Student(3,90,80,70)
stdobj3=Student(4,90,80,70)
stdobj.displayMarks()
stdobj1.displayMarks()
stdobj2.displayMarks()
stdobj3.displayMarks()
print("Total Marks: "+ str(stdobj.getTotalMarks()))
print("Total Percentage: " + str(stdobj.getPercentage()))

stdobj.createExcelofMarks()

