class Employee:
    language = "python" # This is class attribute
    salary = 1700000
    
    def getInfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("good morning")

Sidd = Employee()
Sidd.language = "Javascript" # This is instence attribute

Sidd.greet()
Sidd.getInfo()