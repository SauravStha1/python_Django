class Car:
    brand = "Toyota"
    color = "Red"

    def start(self):
        print("The car is starting...")
#object
my_car = Car()    
print(my_car.brand)   
my_car.start()    

class Student:
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age

    def display(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
s1 = Student("Saurav", 19)
s1.display()