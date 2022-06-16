class Employee:
    company="Goggle"


    def __init__(self,name,salary,subunit):
        print("Employee is created!")

    def getSalary(self,signature):
        print(f"salary for this employee working in {self.company} is: {self.salary}\n{signature}")
    @staticmethod
    def greet():
        print("Good morning,sir ")
    @staticmethod
    def time ():
        print("The time is 9AM in the morning")

harry= Employee("Harry",100,"Youtube")
