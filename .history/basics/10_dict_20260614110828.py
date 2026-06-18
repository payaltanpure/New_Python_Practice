stud= {
    "id":1,
    "name":"Payal",
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
    print("k", ":", v)