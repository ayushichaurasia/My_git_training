class LoanEligibility(Exception):
    def __init__(self, message):
        self.message = message


class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def is_eligible(self):
        if self.salary < 10000:
            return False
        return True


name = input("Enter Your Name: ")
salary = int(input("Enter your salary:"))
pr = Person(name,salary)

if not pr.is_eligible():
    raise LoanEligibility("Sorry!\nYou're not eligible for loan!")
else:
    print("Congrats!\nYou're eligible for loan")
