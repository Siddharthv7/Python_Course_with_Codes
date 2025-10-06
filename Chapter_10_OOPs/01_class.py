class Employee:
    language = "python" # This is class attribute
    salary = 1700000
    
Sidd = Employee()
Sidd.name = "sidd" # This is instence attribute
print(Sidd.name ,Sidd.language, Sidd.salary)

Rohan = Employee()
Rohan.name = "rohon roro"
print(Rohan.name, Rohan.salary, Rohan.language)

# Here name is instance Attribute and salary and language are class
# Attribute as they directly belong to the class

