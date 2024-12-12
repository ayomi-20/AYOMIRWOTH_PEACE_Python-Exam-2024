#Part(ia)
#Object Oriented Programming refers to programming that involes creation of classes which are initialized 
# using the __init__() and constructor instanciated to create objects.
#The creation of a class follows the syntax: class Classname: followed by initialization within which function
# the attributes common to most class objects are passed as parameters and lastly the classes are instanciated. following
# the syntax Classname()  note that the Classname is written begining with a capital letter

#Part(ib)
#A class is a blueprint for how something is done and does not contain real data it could be executing code, while an 
# object is an instance built from a class and it contains real data.

#Part(iii)
def func(a,b):
    return a + b
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
result = (a+b)
print(result)
func(a,b)

#Part(iv)
class Car:
    def __init__(self,brand,name,color):
        self.brand = brand
        self.name = name
        self.color = color
car1=Car("Toyota","Benz","Peach")
car1.brand = "Toyota"
car1.name = "Benz"
car1.color = "Peach"
print(f"My father bought me a brand new {car1.brand} {car1.name} colored {car1.color}")

#Part(v)
class Car:
    def __init__(self,brand,name,color):
        self.brand = brand
        self.name = name
        self.color = color
        
    def start_engine(self):
        print("The engine of the car has started")
car1=Car("Toyota","Benz","Peach")
car1.start_engine()