#list question

'''l = []
count =int(input("please tell how many number you want"))
for i in range(count):
    z = int(input("please tell your number and press enter"))
    l.append(z)
print(l)'''

#l =(input("please tell your numbers separated by spaces").split())
#print(l)

a = [10,20,30,40,50]
b =[]
for i in range(len(a)-1,-1,-1):
    print(a[i])
    b.append(a[i])
print(b)
#3. question to find negative and positive element
'''a = [1,-2,3,-5,-7,5,6,-9]
pos = []
neg = []
for i in a:
    if i>=0:
        pos.append(i)
    else:
        neg.append(i)
print(f"your  positive element is {pos}/n and your negative element is {neg}")'''
#4.print greatest element and index number also
'''list = [1,2,5,4,7,45,56,90]
max = 0
index =0
for i in range(len(list)):
    if list[i]>max:
        max = list[i]
        index = i
print(f"your largest number is {max} at index{index}")'''

#find second greatest element and index too
'''list=[1,2,5,4,7,45,56,90]
max = 0
max2 = 0
index = 0
index2 = 0
for i in range(len(list)):
    if list[i] > max:
        max2 = max
        max = list[i]
        index2 =index
        index = i
    elif list[i] >max2:
        max2 = list[i]
        index2 =i
print(max2,index2)'''


#Sorted  List
a = [1,2,3,4,5,6,7]
for i in range(len(a)-1):
    if a[i] <= a[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("your list is sorted")
