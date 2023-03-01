class Employee:

    def __init__(self, name , salary):
        self.name = name
        self.salary = salary


    def update(self):
        print(f"The Employee",e1.name,"Salary is", e1.salary)
        print(f"The Employee",self.name,"Salary is", self.salary)


e1 = Employee("Praveen",50000)
e1.update()