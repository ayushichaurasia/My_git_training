class VoterAgeException(Exception):
    def __init__(self, message):
        self.message = message

class Voter:
    def __init__(self, age):
        self.age = age

    def validate_age(self):
        if self.age < 18:
            raise VoterAgeException("Sorry!\nYou are not eligible to vote.")
        else:
            return True

age = int(input("Enter your age: "))
v = Voter(age)

try:
    if v.validate_age():
        print("You are eligible to vote.")
except VoterAgeException as e:
    print(e)
