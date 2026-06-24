class demo:
    name1="Payal"
    #instance variable
    name1="Anu"
    def __init__(self):
        #private variable => syntax- __varname
        self.__pin=1234
        #public var
        self.name="Payal"


    #getter method of public type to access privte var __pin outside the class
    def getPin(self):
        #accessed the private var inside the class without getter and setter we done it normally
        return self.__pin
    
    #private method=> syntax- def __methodname(self)
    def __private_method(self):
        #print("Hii")
        return("Its is private method")
    

    #public getter method to access above private method outside the class
    def access_private_method(self):
        return self.__private_method()
    
    #public type setter method to modify the private variables outside the class
    def setPin(self, newpin):
        #accessed the private var inside the class without getter and setter we done it normally
        self.__pin= newpin

obj= demo()

#can't access the private var like this need to build one getter method of public type which will return the private var using self 
# print(obj.__pin)

#called getter method to accesss private variable outside the class but is same file it returns __pin value ,  so this method is called inside the print fucntion
print(obj.getPin())

#called getter method to access private method outside the class
print(obj.access_private_method())

#accessed public var normally
print(obj.name)

#can't access and set, modify the private var outside the class without getter and setter , solutionis below
# __pin=45909
# print(__pin)

#call setter method to set the new pin by accessing old pin private var
obj.setPin(7890)

#again call getter method to check weather the new pin is setted or not
print(obj.getPin())


#how to access forcefully the private var outside the class in same file , inside class we use getter and setter to access
#objectname._classname__private_var_name
#but how and why
# python changes __var to _classname__var
# so internally : print(obj._classname__var)
# this is called name mangling.
print(obj._demo__pin)


#note: if we use any private vairable into code and access it in method to return it always used return statement while accessing it is into that method eg in task_with_exception_handling folder 
#note: if we do not write any return satatement in private method it returns none  by default so, write atleast one return statement in private mthod to avoid none in output


can we access the private var in python outside the class within the child class using getter setter mehods

Yes.

A private variable (__var) cannot be accessed directly in a child class because of name mangling, but it can be accessed indirectly through getter and setter methods inherited from the parent class.

Example
class Parent:
    def __init__(self):
        self.__salary = 50000   # private variable

    def get_salary(self):       # getter
        return self.__salary

    def set_salary(self, salary):  # setter
        self.__salary = salary

class Child(Parent):
    def show(self):
        print(self.get_salary())   # accessing through getter

c = Child()
c.show()

c.set_salary(60000)   # modifying through setter
print(c.get_salary())
Can we access directly in child class?
class Child(Parent):
    def show(self):
        print(self.__salary)   # Error

❌ No, because __salary is mangled to _Parent__salary.

One-line answer

A private variable cannot be accessed directly in a child class, but it can be accessed and modified indirectly through the parent class's getter and setter methods.

is private variable accessible noramaly as public variable into the class not outsid3 the class

Yes. A private variable is fully accessible inside the same class, just like any public variable.

class Student:
    def __init__(self):
        self.__name = "Payal"   # private variable

    def display(self):
        print(self.__name)      # accessible inside class

    def update(self):
        self.__name = "Priya"   # can modify inside class

s = Student()
s.display()

✅ Inside the class:

Read the private variable
Update the private variable
Pass it to methods
Use it in calculations

❌ Outside the class:

s = Student()
print(s.__name)   # Error

❌ Directly in a child class:

class Child(Student):
    def show(self):
        print(self.__name)   # Error
Easy rule
Public (name) → Accessible everywhere.
Protected (_name) → Accessible in class, child class, and outside (by convention).
Private (__name) → Accessible normally only within the same class; outside access requires getter/setter or name mangling (_ClassName__name).