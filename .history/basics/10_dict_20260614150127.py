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

# pop(key)
stud.pop("marks")
print(stud)

# copy
new_built= stud.copy()
print(new_built)



# functions
# min, max, sorted,  len
print(len(dict))
print(max(dict))
print(min(dict))
print(sorted(dict))

