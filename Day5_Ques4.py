
# Ques 4: Create a program to check eligibility of the person for loan  with the help of oops concepts and exception
# handling. Person whose salary is less than 10K/ Month will not be eligible for the loan.


class LoanEligibility(Exception):
    pass


class LoanApplicant:


    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    def check_eligibility(self):
        if self.salary < 10000:
            raise LoanEligibility("Sorry, Your salary is less than 10K/month,\nYou're not eligible for loan!")
        else:
            return True


applicant = LoanApplicant("Ayushi", 10000)

try:
    eligible = applicant.check_eligibility()
    print(applicant.name, "is eligible for the loan")
except LoanEligibility as e:
    print(e)