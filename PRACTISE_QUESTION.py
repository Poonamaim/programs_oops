'''list = ['a','b','c','d']
list2 =[1,2,]
list3 = [3,5,6,7]
list4 = [3,5,8,6,]
c = dict(zip(list,list2))
print(c)
'''
'''a = int(input("enter the total number"))
list1 =[]
list2 = []
for i in range(a):

    x = int(input("enter the lement for firstlist"))
    list1.append(x)
for i in range(a):
    x = input("enter the lement")
    list2.append(x)

dic = dict(zip(list1,list2))
print(dic)
'''
# with the help of zip function we can convert element list to list in dictionary formate
'''emp_id = ['E12','E56','E76','E78']
emp_details = {"fname":"Govind", "lname":"Talde"}'''
'''x =list(emp_details.items())
print(x)'''



'''list =[{"fname":"Poonam", "lname":"ghosh"},{"fname":"sayali", "lname":"balkawade"},{"fname":"komal", "lname":"thorat"}]
new_list = []
'''
'''c =dict(zip(emp_id,emp_details))
print(c)'''

'''dict = {'hi':1,'hello':2, 'guy':3}
res_list = list(dict.values())# for only values
print(res_list)'''

'''my_dict = {
    "language": "Python", "authors": 11, "duration": "30 days"}

result = [*my_dict.values()]
print(result)'''

'''Dict1 = {'Hi': 13, 'Python': 22, 'Tutorial': 15}
list = ['a','b','c','d']
res = list(Dict.items())
print(res)'''
'''c = dict(zip(Dict1,list))
print(c)'''

'''inp_dict =[ {'course':'Web Development','fee':80, 'tutor':'James'}, {'name ':'reena','rollno':1,'class':4}]
for i in inp_dict:
    print(i)

for i in range(0,1):
    print(i)
'''
'''lists = [[2,3,4,5,6,7],
         [8,9,10,11,12],
         [1,2,3,4,5],
         [3,4,5,6,7,9]
         ]
import heapq
merged_list = list(heapq.merge(*lists))'''

#print(merged_list)
'''list1 = [
    [3,4,5,6,7,9],
    [9,8,7,6,5,4,4],
    [2,4,5,67,8],
    [3, 5, 4, 7, 8, 0]
]
import heapq
merge_list = list(heapq.merge(*list1))
print(merge_list)'''

'''n = [100, 200, 300, 400, 500]
for i in range(len(n)-1,-1,-1):
    print(n[i],end=" ")'''

'''list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list1.append(list2)

print(c)
c =list1 + list2
print(c)
'''
'''num= [1, 2, 3, 4, 5, 6, 7]
list= []
for i in num:
    list.append(i*i)
print(list)
# list comprehention we can use
res = [x * x  for x in num]
print(res)'''

'''list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list1.append(list1)'''
'''list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]
print(res)'''

'''list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2):

#for z,n in  zip(list1,list2[::-1]):
    #print(z,n)
    print(x,y)'''
# take two list from user
'''n = int(input("enter the number"))
list1 =[]
list2 =[]
for i in range(n):
    num = int(input("enter the number"))
    list1.append(num)
for i in range(n):
    num1 = input("enter the string")
    list2.append(num1)

c = dict(zip(list1,list2))
print(c)'''
'''num= [1, 2, 3, 4, 5, 6, 7]
list= []
sum =0
for i in num:
    sum =sum + i
print(sum)
list.append(sum*sum)
print(list)
'''

'''list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

res = list(filter(None, list1))
print(res)

list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
index2 = list1.index(25)
# update item present at location
list1[index] = 200
list1[index2] = 100
list1[index2] = 290
print(list1)
print(list1)
print(list)
list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list:
  list.remove(20)
print(list)

'''

'''dict1 = {"name":"poonam","age":"34","mark":"98","id":"123"}
key_list = list(dict1.keys())
key_value = list(dict1.values())
final_dict = {}
# print(key_list[1])
# exit()
for i in range(4,0,-1):
    final_dict[key_list[i]] = dict1.values()[i]
print(final_dict)
exit()
list1 = ["sonam","poonam","akshata","komal"];
list2 = [3,5,7,9];
for i in range(len(list2)-1,-1,-1):
    print(list2[i])

for i in range(len(list1)-1,-1,-1):
    print(list1[i])
'''
#dict2 = {"id":"123","mark":"98","age":"34","name":"poonam"}

'''from collections import OrderedDict
print("The original dictionary : " + str(dict1))
res = OrderedDict(reversed(list(dict1.items())))
print(res)'''

'''for i in range(len(dict1)-1,-1,-1):
    print(dict1[i])'''
'''print(len(dict1))'''
# 1st method

'''print("Keys and Values:")
for key, value in dict1.items():
    print(f"{key}: {value}")'''

# 2nd method
'''reversed_dict = {}
for key, value in dict1.items():
    reversed_dict[value] = key

print(reversed_dict)'''


# 3rd method

'''reversed_dict = {}
while dict1:
    key, value = dict1.popitem()

    reversed_dict[key] = value
    print(reversed_dict)'''
from collections import OrderedDict

dict1 = {"name":"poonam","age":"34","mark":"98","id":"123"}
'''res = OrderedDict(reversed(list(dict1.items())))


print("The dictionary in reversed order : " + str(res))
'''
'''reversed_dict = {}
for key, value in dict1.items():
    reversed_dict[value] = key

print(reversed_dict)
res = {k: reversed_dict[k] for k in sorted(reversed_dict, key=lambda x: list(reversed_dict.keys()).index(x), reverse=True)}


print("The reversed order dictionary : " + str(res))'''
r'''eversed_dict = {}
while dict1:
    key, value = dict1.popitem()
    print(dict1)
    reversed_dict[key] = value

print("The reversed order dictionary : " + str(reversed_dict))'''
'''dic = {
    "name" :"poonam",
    "cgpa" : 9.6,
    "marks" : [98,97,95]

}
print(dic)'''
student = {
    "names " : "poonam",
    "subjects": ["python","c","java"],
    "topics" : ("dict","set"),
    "age" :35,
    "is_adult" : True,
    "marks" : 96.4
}

print(student["age"])
print(student["topics"])

