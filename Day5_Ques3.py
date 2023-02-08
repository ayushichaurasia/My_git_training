
# Ques 3: Create a program to validate the age of the voter with the help of custom exception. Voters whose age is less
# than 18 should not be allowed to vote.

class Voting(Exception):
    pass


def vote(age):
    if age < 18:
        raise Voting("Sorry,You are not eligible for voting!\nThank You!")
    else:
        print("Welcome to voting system!\nThank You!")


try:
    age = int(input("Enter your age: "))
    vote(age)

except Voting as e:
    print(e)
