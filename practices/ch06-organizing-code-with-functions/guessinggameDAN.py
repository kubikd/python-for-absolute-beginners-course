import random


def main():
    show_header()
    play_game(0, 5)


def show_header():
    print("------------------------------")
    print("     M&M guessing game!")
    print("------------------------------")
    print()
    print("Guess the number of M&Ms and you get lunch on the house!")
    print()


mm_count = random.randint(1, 100)


def play_game(attempts, attempt_limit):
    while attempts < attempt_limit:
        guess_text = input("How many M&Ms are in the jar? ")
        guess = int(guess_text)
        attempts += 1

        if mm_count == guess:
            print()
            print(f"YOU WIN! The number was {guess}.")
            print()
            break
        elif guess < mm_count:
            print("SORRY, that's too LOW!")
        else:
            print("SORRY, that's too HIGH!")
    print()
    print(f"SORRY, you tried {attempts} times!  You are out of attempts")
    print(f"The number of M&Ms is {mm_count}")
    print()


if __name__ == "__main__":
    main()
