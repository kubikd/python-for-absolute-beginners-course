import random

print("--------------------------------------------------")
print("              M&M Guessing Game!")
print("--------------------------------------------------")
# print(mm_count)

print("Guess the number of M&Ms and you get lunch on the house!")
print()

mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    guess_text = input("How many M&Ms are in the jar? ")
    guess = int(guess_text)
    attempts += 1

    if mm_count == guess:
        print(f"You get a free lunch! It was {guess}.")
        break
    elif guess < mm_count:
        print("Sorry, that's too LOW!")
    else:
        print("That's too HIGH!")

print(f"The number of M&Ms is {mm_count}")
print(f"You guessed the number of M&Ms in {attempts} tries!")

