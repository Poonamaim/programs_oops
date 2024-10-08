# dictionary ke andar duplicate key nhi ho sakti

'''dict= {
    "names" : "poonam",
    "subjects": ["python","c","java"],
    "topics": ("dict","set"),
    "age": 35,
    "is_adult" : True,
    "marks" : 96.4
}'''

'''print(dict["age"])
print(dict["topics"]) # topics dega
print(["names"])''' # name dega

'''dict ["names"] = "poonam" # value add karega
dict["name"] = "pooja"
dict["surname"] = "jain"
print(dict)'''

'''null_dict ={}
null_dict["apna college"] ="pooja"
student = {
    "name " : "rahul ghosh",
    "subject" : {
        "phy" :97,
        "chem" :98.9,
        "math" : 95


    }
}'''
'''print(student["subject"])
print(student["subject"]["chem"])
print(student["subject"]["math"])
print(student.keys())
print(len(student.keys()))
print(student.values())
print((list(student.values()))) # values
print(student.items())

pairs = list(student.items())
print(pairs[0])'''

'''# myDict.get("key") =return the value according to value
#myDict.item()

print(student["name"])
print(student.get["name"])'''


'''students = {
    "name" : "rahul ghosh",
    "subjects" : {
        "phy" :97,
        "chem" :98.9,
        "math" : 95


    }
 }'''

'''#print(students["name2"]) # it will get error eske baad ka code nhi run nhi hoga
print(students.get("name2")) # it will give none after the code will run 
print("hello")'''



#update method
'''students.update({"city": "delhi","age":"16"})
print(students)

#set = collection of unorder item
#each element in the set must be unique and immutable
# int ,float, string , tuple ,True,False = we can store
# inside of set we can not store list and dictionary
nums = {2,2,4,4,6,7,8,"hello","gun"} # it will ignore duplicate value and unorderd

nums1 = {3,4,6,8,"pooja","seeta",4,7} # ignore the 4 it will print 4 only onces
print(nums1)
print(len(nums1))
c ={}# this is a dictionary
type1 = set() # empty set
print(type(type1))'''

#set method = add method
#set = set are mutable
# set = inside of element are immutable
'''collection =set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add(4)
collection.add("hello")
collection.add((1,2,3,4))
#collection.add({"hi":"suma"}) can,t add dictionary and list inside of set
print(collection)

#2nd method (clear)
collection.clear()
print(len(collection))
print(collection.pop())
print(collection.pop())
# union and intersection'''

'''set ={1,2,3,4}
set2 = {4,5,6,7,9}
print(set.union(set2))
print(set.intersection(set2))
print(set.difference(set2))


person = {"name": "John", "age": 30}
print(person["name"]) # john-
print(person["name"])
print(person["age"])
person["name"]  ="rohit"'''

'''dict1 = {'color': 'blue', 'shape': 'circle'}
dict2 = {'color': 'red', 'number': 42}

dict1.update(dict2)
print(dict1)'''
ex_dict = {"a": "anteater", "b": "bumblebee", "c": "cheetah","name":"pooja"}

'''print(ex_dict.keys())
#dict_keys(['a', 'b', 'c'])

ex_dict.values()
print(ex_dict.values())
#dict_values(['anteater', 'bumblebee', 'cheetah'])

ex_dict.items()
print(ex_dict.items())
# dict_items([('a', 'anteater'), ('b', 'bumblebee'), ('c', 'cheetah')])'''

'''if "name" in ex_dict:
    print("Key 'name' exists.")
    print("pooja")
else:
    print("key is not exist")

#ex_dict["city"] = "New York" output = add kr dega value dictionary mai
print(ex_dict)
del ex_dict["name"]
# before ={'a': 'anteater', 'b': 'bumblebee', 'c': 'cheetah', 'name': 'pooja'}
print(ex_dict) # after {'a': 'anteater', 'b': 'bumblebee', 'c': 'cheetah'}

'''
'''for key in ex_dict:
    print(key)

for value in ex_dict.values():
    print(value)
# output


for key, value in ex_dict.items():
    print(key, value)'''
# output
'''a anteater
b bumblebee
c cheetah
name pooja'''

'''dict= {"a": 6, "b": 2}
dict1 = {"a": "pooja", "b": "fool"}
dict2 = {"b": 3, "c": 4}

# merge for two dictionary with the help of merge funtion
merged_dict = {**dict1, **dict2}

# Create a dictionary where the values are squares of the key
squares = {x: x**2 for x in range(1, 6)}
print(squares)

#Find the key with the maximum value in a dictionary.
max_key = max(dict1, key=dict1.get) # it will find max key vased on value
print(max_key)

max_key = max(dict,key=dict.get)
print(max_key)

nested_dict = {"first": {"a": 1, "b": 2}, "second": {"c": 3, "d": 4}}
print(nested_dict)
print(nested_dict["first"])
print(nested_dict["second"])
'''

dictionary = {"name":"poonam","lastname":"ghosh","roll no":23,"subject":["science","math"]}

for dict in dictionary:  # it will print key
    print(dict)

for dict in dictionary:
    print(dictionary[dict]) # it will print value

for dict in dictionary:
    print(dict,dictionary[dict]) # it will print key and value

for key, value in dictionary.items(): # it will print key and value
    print(key,value)

if "name" in dictionary:
    print("poonam")
print(len(dictionary))

dictionary["marks"] = [90,89,90]
print(dictionary)

del dictionary["name"]
print(dictionary)







