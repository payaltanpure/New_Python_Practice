# to run both child classes at a time import both child classes in one sep file and then call parent class and child class methods from that location by creating objects of child class
from developer import dev
from tester import tester


d= dev(1, "Payal", 34000, "Python")
d.display()
d.coding()

print("-----------------------")

t= tester(2, "Anu", 55000, "Llama")
t.display()
t.testing()