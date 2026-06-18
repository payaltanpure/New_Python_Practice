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

for key, value in stud:
    print("Key")