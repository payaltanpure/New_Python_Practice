s="I, am, payal"
print(s)
print(type(s))
print(id(s))
print(len(s))
words= s.split(",")
print(words)
print(type(words))
print(id(words))
print(len(words))

string= "a"
print (id(string))
string="b"
print (id(string))

# output
# 140728793532000
# 140728793225040
# differnt address becoz we do not pass any datatype so varibale created duplicate byt on diff memory locations

string.add('k')
print(string)