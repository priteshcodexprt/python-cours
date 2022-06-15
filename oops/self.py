class Employee:
    company="Goggle"
    def getsalary(self):
        print(f"salary is {self.salary}")

harry=Employee()
harry.salary=100000
harry.getsalary()