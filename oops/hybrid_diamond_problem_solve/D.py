from B import B
from C import C

class D(B,C):

    def __init__(self,name, salary, age ):
        print("D cons")
        #using **kwargs we set value to all para of A, B, C in key value pair format so the confusion of para passing is avoided and twice setting value to grand parent class para cons var is also avoided by avoiding the writing of grand parents para cons variables into middle level childs para cons and calling the parent class para cons twicely is also avoided by single super()
        #call to B, C para cons, and set value to var according to repective parameters set in key value pair here 
        super().__init__(
            name= name ,
            salary= salary,
            age= age )
        


d= D("Payal", 1000, 10)
print(D.mro())

# D cons
# B con
# 1000
# A con Payal
# C con
# 10
# A con Payal
# [<class '__main__.D'>, <class 'B.B'>, <class 'C.C'>, <class 'A.A'>, <class 'object'>]

# A con Payal this constructor of grand parent class is called twice this diamond problem 
# why this A's con is called twice becoz we called it from iths two child classes B and C also , so twice it is called and two times the value to name var is set which is not valid this is
#called as diamond problem 

# solution to this is super() call with **kwargs
#using this we call the cons of grand parent A only once and also the value to the var of grand parent A class is set once only 
#and we use super() call to call grand parent class para cons from child class D super().__init__(self, name, salary, age) , but in that compiler gets confused that to which parent calss weather B or C should receive which para so we uses
# single  super call and key value pairs in it to specify which value should be passed to which para cons

#after solution applied output is as below:
# D cons
# A con Payal
# C con
# 10
# B con
# 1000
# [<class '__main__.D'>, <class 'B.B'>, <class 'C.C'>, <class 'A.A'>, <class 'object'>]

# A con Payal called only once not twice and also value to name var of A class a=setted only once using kwargs and confusion of passing para to para cons of parent classes using super is also resolved using key value pairs of **kwargs