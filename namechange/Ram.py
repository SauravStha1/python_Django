class Employee:
    def __init__(self, name, age, salary):
        self.n = name
        self.a = age
        self.s = salary
    
    def Inc_Salary(self):
        print(F"Old salary = {self.s}")
        self.s = self.s * 0.2 + self.s
        return self.s  
    
    def printSalary(self):
        print(f"New Salary is {self.s}")

e1 = Employee("Saurav", 19, 2000)
e2 = Employee("Sarrok", 20, 3000)
e2.Inc_Salary()
e2.printSalary()