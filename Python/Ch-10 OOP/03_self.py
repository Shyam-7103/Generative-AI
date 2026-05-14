class Employee:
    language = "Python" # Class Attributes
    salary = 12000

    def getInfo(self):
        print(f"The language is {self.language}, the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


Luffy = Employee()
# Luffy.name = "Monkey.D.Luffy" # Instance Attributes
# Luffy.language = "JavaScript"
# print(Luffy.name, Luffy.language, Luffy.salary) 

# Employee.getInfo(Luffy)
Luffy.getInfo()

# Luffy.greet()
Employee.greet()

