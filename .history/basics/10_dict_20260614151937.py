stud= {
    "name":"Payal",
    "id":1,
    "marks":60.70
}

print(stud)
print(type(stud))

# access dict by keys
print(stud["name"])

# inbuild methods get to access dict 
print(stud.get("id"))

# update
stud["id"]= 2
print(stud)

# loop

for ch  in stud:  #into ch we get all keys and then access that keys value by indexing using key 
    print(ch,":",stud[ch])

for k, v in stud.items():
    print(k, ":", v)


# inbuilt methods

# 1. keys
print(stud.keys())

# 2.values
print(stud.values())

# items
print(stud.items())

# pop(key) and popitem()-last ele remove
stud.pop("marks")
print(stud)
stud.popitem()
print(stud)

# copy
new_built= stud.copy()
print(new_built)

# update- add/update
stud.update({"loc":"Pune", "div":"A"})
print(stud)
stud.update({"loc":"mumbai"})
print(stud)

# setdefault(key, value): if any key forget to add wecan add by this method, if not present it will be added in dict if present prior ignored it 
stud.setdefault("passoutyear", "0")
print(stud)


# functions
# min, max, sorted,  len
print(len(stud))
print(max(stud))
print(min(stud))
print(sorted(stud))

# user input

cars={}
cars["model_no"]= int(input("Enter model no"))
cars["name"]= input("ENter name of car")
cars["Price"]= float(input("Enter price:"))
print(cars)

print(cars["model_no"])

players={
    "rohit":100,
    "dhoni":99,
    "sachin":101,
    "virat":
}