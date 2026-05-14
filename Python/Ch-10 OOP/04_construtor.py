class Employee:
    language = "Python" # Class Attributes
    salary = 12000

    def __init__(self, name, salary, language): # dunder_method,which is automatically called whenever new object is created

        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}, the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


Luffy = Employee("Zoro", 22000, "NODEJS")
# Luffy.name = "Monkey.D.Luffy"
print(Luffy.name, Luffy.salary, Luffy.language)

