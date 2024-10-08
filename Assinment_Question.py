# first assinment
'''sum =0
x =[]
while(True):

    user_input =input("enter the price:/n")
    if (user_input != "q"):
        sum = sum + int(user_input)
        print(f"order total so far: {sum} ")
        x.append(user_input)

    else:
        a=0
        for i in x :
            a+= 1
            print(f".{a}>{i}")

        print("")
        print(f"your bill  total is {sum} . thanks for come")
        break'''
'''##factorial
#part = find of traviling 0 in this number(n-1)
def factorial(n):
    if n ==0 or n ==1:
        return 1
    else :
        return n * factorial(n-1)
def factorialTraversingZeros(n):
    fac = factorial(n)
    print(fac)
    count = 0
    while(fac % 10 ==0):
        count = count + 1
        fac = fac /10
        return count

if __name__ == "__main__":
     n = int(input("enter a number"))

     fac = factorial(n)
     print(f"the factorial is {fac}")
     print(factorialTraversingZeros(10))'''
#3
 #count positive number
'''number = int(input ("enter the range of number times you want"))
list = []
for i in range(number):

    n = int(input("enter the number"))
    list.append(n)
print(list)

count = 0
for i in list:
   # print(i)

   # count =0

    if i >0:

        count = count +1

print(count)'''
#4
# calculate even given number
'''list =[]
n = int(input("enter the number how many you want"))
for i in range(1,n+1):

    n1 = int(input("enter the number which you want"))
    list.append(n1)

print(list)
sum =0
count =0
for i in list:

    if i % 2 ==0 :
        count = count+1 # counting even number

        sum = sum+i # print the sum
print(sum)
print(count)'''
#5
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
#6
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
#7
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
#8
## user se input lena hai jab tak bo 7 to 10
'''while True:
    number = int(input("enter the number 1 < 10: "))
    if 1 <= number <= 10:
        print("you rigth")
        break
    else:
        print("envalid number try again")'''
#9
# prime numbeber
'''n = int(input("enter the number"))
is_prime = True
if n > 1:
    for i in range(2,n):
        if (n % i) == 0:
            is_prime = False
            print(" not prime")
            break
        else:
            print(" prime")
            exit()'''
#10
# find unique item

#item = ["apple","banana","orange","apple","mango"]
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
#11
# times based
'''import time

wait_time = 1
max_retrimes = 5
attemps = 0

while attemps < max_retrimes:
    print("attemps", attemps + 1, "wait_time", wait_time, )
    time.sleep(wait_time)
    wait_time *= 2
    attemps += 1'''

# iteration tool
# (for,comprehension)
# iterable objects (list,string,file)
# (__next__ =response)

#12
'''emp_id = ['E12','E56','E76','E78']
emp_details = [{"fname":"Govind", "lname":"Talde"},{"fname":"Poonam", "lname":"ghosh"},{"fname":"sayali", "lname":"balkawade"},{"fname":"komal", "lname":"thorat"}]
new_list = []
c =dict(zip(emp_id,emp_details))
print(c)
'''#13
'''
str = "hello gu#ys how are you"
dig = 0
chr =0
spchr = 0

for i in str:
    if i.isdigit():
        dig = dig+1
    elif i.isalpha():
        chr =chr+1
    else:
        spchr =spchr+1
print(dig+chr+spchr)'''
'''a= "you brOther hoW are YOU"
b = " "
for i in a :
    if i.islower():
        b = b+i

for i in a:
    if i.isupper():
        b=b+i

print(b)'''

#14 count digit, alpha,
'''
str = "pooja@12334$"
chr =0
dig = 0
spchr =0
for i in str:
    if i.isdigit():
        dig = dig+1
    elif i.isalpha():
        chr = chr+1
    else:
        spchr = spchr+1
print(dig+chr+spchr) '''


a = "hello how are you guys"
vowels =0;
const = 0;
for i in a:
    if i in "AIOUEaioue":
        vowels =vowels+1
    elif i== " ":
        continue
    else:
        const =const+1
print(f"your vowels are {vowels} and your const are {const}")





