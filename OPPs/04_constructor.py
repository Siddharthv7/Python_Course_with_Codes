class Employee:
    language = "python" # This is class attribute
    salary = 1700000
    
    def __init__(self, name, salary, language):# dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
    
    def getInfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("good morning")

Sidd = Employee("sidd", 2300000, "Javascript")
# Sidd.name = "sidd"
print(Sidd.name, Sidd.salary, Sidd.language)

