'''n = int(input("enter the number"))
for i in range(1,11):
    if i ==5:
        continue
    print(n,'x',i,'=',n*i)'''

# reverse string
'''list =[]
n = int(input("enter the string number"))
for i in range(n):
    n1 =input("enter the string")
    list.append(n1)

print(list)
for i in range(len(list)-1,-1,-1):
    print(list[i])'''

'''list =[]
n = int(input("enter the string number"))
for i in range(n):
    n1 =input("enter the string")
    list.append(n1)

print(list)
reverse =""
for char in list:
    reverse = char + reverse
    print(" ")
print(reverse,end = " ")'''

# find first not repeated character
'''str = input("enter the string")

for char in str:
    if  str.count(char) == 1 :
        print("character is : ", char)
        break # first character pr loops terminate ho jayega


str = input("enter the string")

for char in str:
    if  str.count(char) == 1 :
        print("character is : ", char) # second character pr loops terminate ho jayega

        '''

# factorial calculator
'''def fctorial(n):
    if n ==0 or n == 1:
        return 1
    else:
        return n * fctorial(n-1)

c =fctorial(7)
print(c)'''
'''
number =7
factorial=1
while number >0:
    #factorial = factorial * number
   # factorial = number-1
    factorial *=  number
    number -= 1
print(factorial)'''

# user se input lena hai jab tak bo 7 to 10
while True:
    number = int(input("enter the number 1 < 10: "))
    if 1 <= number <= 10:
        print("you rigth")
        break
    else:
        print("envalid number try again")
        '''

# prime numbeber
'''
        n = int(input("enter the number"))
is_prime = True
if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            is_prime = False
            print(" not prime")
            break
        else:
            print(" prime")
            exit()

# find unique item

# item = ["apple","banana","orange","apple","mango"]
'''list =[]
item1 =int(input("enter the item"))
for i in range(item1):
    item = input("enter the item")
    list.append(item)
print(list)
unique_item = set()
for items in list:
    if items in unique_item:
        print("duplicate: ",item)
        break
    else:
      unique_item.add(items)
'''
# times based
import time

wait_time = 1
max_retrimes = 5
attemps = 0

while attemps < max_retrimes:
    print("attemps", attemps + 1, "wait_time", wait_time, )
    time.sleep(wait_time)
    wait_time *= 2
    attemps += 1

# iteration tool
# (for,comprehension)
# iterable objects (list,string,file)
# (__next__ =response)