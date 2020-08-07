import random


def main():
    show_header

    player = "Dan"
    ai = "Computer"

    play_game(player, ai)


def show_header():
    print("--------------------------------------------------")
    print("            Rock paper Scissors v1")
    print("--------------------------------------------------")


def play_game(player_1, player_2):

    rolls = ['rock', 'paper', 'scissors']

    roll1 = get_roll(player_1, rolls)

    roll2 = random.choice(rolls)

    print(f"{player_1} roll {roll1}")
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
            winner = player_1

    print("The game is over!")
    if winner is None:
        print("It was a tie!")
    else:
        print(f'{winner} takes the game!')


def get_roll(player_name, rolls):
    roll = input(f"{player_name}, what is your roll? rock, paper, or scissors?: ")
    roll = roll.lower().strip()
    if roll not in rolls:
        print(f"Sorry {player_name}, {roll} is not a valid play!")
        return none
    
    return roll

if __name__ == "__main__":
        main()
