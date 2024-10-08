#a ="brother"
#b = ""
#for i in range(len(a)-1,-1,-1):
  #  b=b+a[i]
#print(b)'''
#2.reverse
#print(a[::-1])

#2
'''a = "you brOther hoW are YOU"
b = " "
for i in a :
    if i.islower():
        b = b+i
for i in a:
    if i.isupper():
        b=b+i

print(b)
'''
#3.count all letter ,digits,specialcharacter
'''str = "pooja@12334$"
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
print(dig+chr+spchr)'''

'''
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
print(f"your vowels are{vowels} and your const are{const}")
'''


#
'''
def vowelscounter(x):
    vowels = 0
    const = 0

    for i in x:
        if i in "AIOUEaioue":
            vowels =vowels+1
        elif i ==" ":
            continue
        else:
            const = const+1
    return vowels,const
a="hello guys how are you"
print(vowelscounter(a))
'''
'''str = "hello gu#ys how are you"
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


'''list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# remove None from list1 and convert result into list
res = list(filter(None, list1))
print(res)'''