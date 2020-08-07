import random

print("--------------------------------------------------")
print("            Rock paper Scissors v1")
print("--------------------------------------------------")

player_1 = "You"
player_2 = "Computer"

rolls = ['rock', 'paper', 'scissors']

print(rolls)
print(player_1)
print(player_2)

roll1 = input(f"{player_1}, what is your roll? rock, paper, or scissors: ")
roll1 = roll1.lower().strip()
if roll1 not in rolls:
    print(f"Sorry {player_1}, {roll1} is not a valid play!")

roll2 = random.choice(rolls)

print(f"{player_1} rolls {roll1}")
print(f"{player_2} rolls {roll2}")

# Test for a winner
winner = None

if roll1 == roll2:
    print("The play was tied!")
elif roll1 == 'rock':
    if roll2 == 'paper':
        winner = player_2
    elif roll2 == 'scissors':
        winner = player_1
elif roll1 == 'paper':
    if roll2 == 'scissors':
        winner = player_2
    elif roll2 == 'rock':
        winner = player_1
elif roll1 == 'scissors':
    if roll2 == 'rock':
        winner = player_2
    elif roll2 == 'paper':
        winner == player_1

print("The game is over!")
if winner is None:
    print("It was a tie!")
else:
    print(f'{winner} takes the game!')
