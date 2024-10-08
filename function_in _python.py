'''def hello(a):
    print(a) # perameter

hello(12)# Argumen

#
def hello(a,b,c,d =40):
    print(a+b+c+d) #perameter

hello(12,14,15,78)# Argument'''

#default and keyword argumenrt
'''def hello(a,b,c,d =40):
    print(a+b+c+d) #perameter

hello(a=12,b=14,c=15,d=78)# Argumen'''

#def evenodd(a):
   # if a%2 ==0:
      #  print("even")
   # else:
    #  print("odd")
    
#evenodd(12)
#evenodd(31)
#evenodd(23)
#evenodd(16)

#print vs return
def evenodd(a):
    if a % 2 == 0:
        return("even")
    else:
        return("odd")


print(evenodd(12))
print(evenodd(31))
print(evenodd(23))
print(evenodd(16))

