class demo2:
   
   def __init__(self):
        self.__pin= 1090

   def update(self):
       #here inside the class the private member is accssed without any getter setter method
       self.__pin=6789
       print(self.__pin)

   def getter(self):
       return self.__pin
       

obj= demo2()
obj.update()
# print(obj.__pin)
# AttributeError: 'demo2' object has no attribute '__pin'
#so we have to craete getter setter method to access private menbers outside the class and call that methods using object name 
print(obj.getter())

can we access the private var in python outside the class within the child class using getter setter mehods

# Yes.

# A private variable (__var) cannot be accessed directly in a child class because of name mangling, but it can be accessed indirectly through getter and setter methods inherited from the parent class.

# Example
# class Parent:
#     def __init__(self):
#         self.__salary = 50000   # private variable

#     def get_salary(self):       # getter
#         return self.__salary

#     def set_salary(self, salary):  # setter
#         self.__salary = salary

# class Child(Parent):
#     def show(self):
#         print(self.get_salary())   # accessing through getter

# c = Child()
# c.show()

# c.set_salary(60000)   # modifying through setter
# print(c.get_salary())
# Can we access directly in child class?
# class Child(Parent):
#     def show(self):
#         print(self.__salary)   # Error

#  No, because __salary is mangled to _Parent__salary.

# One-line answer

# A private variable cannot be accessed directly in a child class, but it can be accessed and modified indirectly through the parent class's getter and setter methods.

# is private variable accessible noramaly as public variable into the class not outsid3 the class

# Yes. A private variable is fully accessible inside the same class, just like any public variable.

# class Student:
#     def __init__(self):
#         self.__name = "Payal"   # private variable

#     def display(self):
#         print(self.__name)      # accessible inside class

#     def update(self):
#         self.__name = "Priya"   # can modify inside class

# s = Student()
# s.display()

#  Inside the class:

# Read the private variable
# Update the private variable
# Pass it to methods
# Use it in calculations

# ❌ Outside the class:

# s = Student()
# print(s.__name)   # Error

# ❌ Directly in a child class:

# class Child(Student):
#     def show(self):
#         print(self.__name)   # Error
# Easy rule
# Public (name) → Accessible everywhere.
# Protected (_name) → Accessible in class, child class, and outside (by convention).
# Private (__name) → Accessible normally only within the same class; outside access requires getter/setter or name mangling (_ClassName__name).