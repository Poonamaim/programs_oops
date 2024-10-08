'''for i in range(0,10,2):
    print(i)'''

'''l1 = ["eat", "sleep", "repeat"]

for count, ele in enumerate(l1): # it will print each element with index number
    print (count, ele)

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)'''

'''l = ["geeks", "for", "geeks"]

for i in range(len(l)):
    print(i)

Numbers =[y for y in range(11)]

print(Numbers)'''

'''d = dict()

d['xyz'] = 123
d['abc'] = 345
d['name'] = "pooja"
d["roll no"] = 2
d['subject'] = {"math":34,"science":35,"english":36}

print(d)'''
'''for i in d:
    print("% s % d" % (i, d[i]))'''
'''t = ((1, 2), (3, 4), (5, 6))
for a, b in t:
    print(a, b)
    

fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit, color in zip(fruits, colors):
    print(fruit, "is", color)



for letter in 'geeksforgeeks':

    if letter == 'e' or letter == 's':

        continue
    print('Current Letter :', letter)

for letter in 'geeksforgeeks':

    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'z' or letter == 's':
        break
print(letter)

for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break\n")# in tis loops after the finishing of for range else part also will run

clothes = ["shirt", "sock", "pants", "sock", "towel"]
emp_list = []
for i  in clothes:
    if i == "sock":
        continue
    else:
        print("yes clothes")
emp_list.append("socks")
print(emp_list)

for day in range(1, 8):
    distance = 3 + (day - 1) * 0.5
    print(f"Day {day}: Run {distance:.1f} miles")

for index, num in enumerate([10, 20, 30]):
    print(f'Index {index}: {num}')
num =[10,20,30]
for index, num in enumerate(num):
    print(f'Index {index}: {num}')

#Iterating over a dictionary
person = {'name': 'John', 'age': 30}
for key, value in person.items():
    print(key,value)
'''
'''s = "Geeks"
for i in s:
    print(i)

for i in range(0, 10, 2):
    print(i)
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s %d" %(i, d[i]))'''

import re
#email_condition = "^[a-z]+[\._]?[a-z 0-9] + [@]\w+ [.]\w{2,3}$ "

email_condition = "^[a-zA-Z0-9._%±]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$"
user_email = input("Enter Your Email")


if re.search(email_condition, user_email):
    print("Right Emails")
else:
    print("wrong condition")