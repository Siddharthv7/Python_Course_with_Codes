class Programmer:
    company = "Google"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
        
p = Programmer("Sidd", 1400000, 2434201)
print(p.name, p.salary, p.pincode)
A = Programmer("Parth", 1400000, 2434201)
print(A.name, A.salary, A.pincode)