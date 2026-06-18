import module as a
a.add(10,20,30,40,50)
a.mul(2,3)


# here access to add fun is only given
from module import add 
add(1,2,3,4,5)
#mul(2,3)

#to import all functions from module
from module import *