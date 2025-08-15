# how to initiate a class

class Employee:
    def __init__(self):
        self.id = 121
        self.salary = 50000 
        self.designation = "SDE"
    
    def travel(self,destination):
        print(f"Employee is not traveling to {destination}")

# create an object / instance of the class

sam = Employee()
print(sam.salary)
print(sam.travel(85))