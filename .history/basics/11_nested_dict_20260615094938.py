s={
    "id":101,
    "name": "Payal",
    "add":{"pincode":410505,
           "city":"Pune",
           "state":"Maharashtra"
           }
}

print(s)
print(s.keys())
print(s["add"])
print(s["add"]["city"])

print(type(s))
print(type(s["add"]))

 
for keys, values in s.items():
    if type(values)==dict:
        for nested_key, nested_values