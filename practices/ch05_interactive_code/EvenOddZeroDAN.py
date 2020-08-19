print("----------------------------------------------")
print("         Even/Odd/Zero Identifier")
print("----------------------------------------------")

user_num = 1
user_int = int(user_num)
while user_int != 0:
    user_num = input("Enter any whole number or enter Zero to Stop Playing: ")
    user_int = int(user_num)
    rem = user_int % 2
    if user_int == 0:
        print("You entered Zero.  Thank you for playing!")
        print()
        print()
    elif rem == 0:
        print("The number entered is EVEN!")
        print()
        print()
    else:
        print("The number entered is ODD!")
        print()
        print()
