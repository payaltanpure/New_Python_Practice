s={
    "id":101,
    "name": "Payal",
    "add":{
            "city":"Pune",
           "state":"Maharashtra"
            "pincode":410505
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
        for nest_key,nest_val in keys.items():
            print(nest_key)
    print(keys)