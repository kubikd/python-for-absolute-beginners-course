print("----------------------------------------------")
print("         Even/Odd Number Identifier")
print("----------------------------------------------")

play_again = 'Y'

while play_again == 'Y':
    user_num = input("Enter any whole number: ")
    user_int = int(user_num)
    if user_int % 2 == 0:
        print("The number entered is EVEN!")
        print()
        print()
    else:
        print("The number entered is ODD!")
        print()
        print()
    play_again = input("Do you want to try again? (Y/N)")

    if play_again == 'N':
        print("Thank you for playing!")
        print()
        print()
