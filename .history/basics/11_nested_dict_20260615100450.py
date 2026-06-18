# s={
#     "id":101,
#     "name": "Payal",
#     "add":{
#             "city":"Pune",
#             "state":"Maharashtra",
#             "pincode":410505
#            }
# }
# # city , state and pincode are the values of add key and pune , maha, 41050 are the values of keys city, state and pincode

# print(s)
# print(s.keys())
# print(s["add"])
# print(s["add"]["city"])

# print(type(s))
# print(type(s["add"]))

 
# for keys, values in s.items():
#     if type(values)==dict: #becoz the city , pincode and state are the values of outer dict key add , so we have to check values type == dict then run inside for loop
#         for nest_key,nest_val in values.items(): #extract keys and values both of the value of add key by items() method and then print only nested_keys from it
#             print(nest_key)
#     print(keys)


# a={
#     "id": "101",
#     "marks": [10,20,30]
# }

# print(a)

# for keys in a:
#     print (keys)

# for values in a.values():
#     print(values)

# for k, v in a.items():
#     print(k , v)

# for values in a.values(): #101, [10,20,30]
#     if type(values)==list: #[10,20,30] cond true
#         for items in values: #items= 10,20,30 one by one  form values
#             print (items) #print 10, 20 ,30
#     else:
#         print(values) #printed 101



