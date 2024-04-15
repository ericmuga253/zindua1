import random

# Dictionary representing the positions of snakes and ladders
snakes_ladders = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}

# Function to roll a dice
def roll_dice():
    return random.randint(1, 6)

# Function to move the player
def move_player(player, dice_roll):
    new_position = player + dice_roll
    if new_position in snakes_ladders:
        new_position = snakes_ladders[new_position]
        print("Oops! You encountered a snake or ladder! You are now at position", new_position)
    else:
        print("You rolled a", dice_roll, "and moved to position", new_position)
    return new_position

# Function to check if the player has won
def has_won(player_position):
    return player_position >= 100

# Main function to play the game
def play_game():
    player1_position = 0
    player2_position = 0
    current_player = 1

    while True:
        input("Player " + str(current_player) + ", press Enter to roll the dice...")
        dice_roll = roll_dice()
        print("Player", current_player, "rolled a", dice_roll)

        if current_player == 1:
            player1_position = move_player(player1_position, dice_roll)
            if has_won(player1_position):
                print("Congratulations! Player 1 has won!")
                break
            current_player = 2
        else:
            player2_position = move_player(player2_position, dice_roll)
            if has_won(player2_position):
                print("Congratulations! Player 2 has won!")
                break
            current_player = 1

# Start the game
play_game()