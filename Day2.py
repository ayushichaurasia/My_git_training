#1st question
a=[1,2,3,4,5,6]
print(a[1:5])


#2nd question
string = input("Enter a string:")
if string == string[::-1]:
    print("This is palindrome.")
else:
    print("This is not palindrome.")


#3rd question
String = input("Enter a string: ")
repeated_char = []
for char in String:
    if String.count(char) > 1:
        if char not in repeated_char:
            repeated_char.append(char)
print("Repeated letters are: ", *repeated_char)


#4th question

def slicing():

    list = (input("Enter a list: "))
    new_list = list.split()
    print("Your list: ", new_list)
    print("Sliced list: ",new_list[1:5])
    print("\n")

slicing()

def palindrome():

    string = input("Enter a string:")
    if string == string[::-1]:
        print(string," is palindrome.")
        print("\n")
    else:
        print(string," is not palindrome.")
        print("\n")

palindrome()

def repeat_character():

    Str = input("Enter a string: ")
    repeated_char = []
    for char in Str:
        if Str.count(char) > 1:
            if char not in repeated_char:
                repeated_char.append(char)
    print("Repeated letters are: ", *repeated_char)


repeat_character()