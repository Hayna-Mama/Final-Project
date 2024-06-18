import random

def roll_dice():
    return random.randint(1, 6)

def play_round(player1, player2):
    player1_roll = roll_dice()
    player2_roll = roll_dice()
    
    print(f"{player1} rolls: {player1_roll}")
    print(f"{player2} rolls: {player2_roll}")
    
    if player1_roll > player2_roll:
        print(f"{player1} wins this round!\n")
        return player1
    elif player2_roll > player1_roll:
        print(f"{player2} wins this round!\n")
        return player2
    else:
        print("It's a tie! No one wins this round.\n")
        return None

def dice_rolling_game():
    player1 = input("Enter the name of Player 1: ")
    player2 = input("Enter the name of Player 2: ")
    
    player1_wins = 0
    player2_wins = 0
    rounds = 3
    
    for i in range(rounds):
        print(f"Round {i+1}:")
        winner = play_round(player1, player2)
        
        if winner == player1:
            player1_wins += 1
        elif winner == player2:
            player2_wins += 1
        
        if player1_wins == 2:
            print(f"{player1} wins the game!")
            break
        elif player2_wins == 2:
            print(f"{player2} wins the game!")
            break
    
    if player1_wins < 2 and player2_wins < 2:
        if player1_wins > player2_wins:
            print(f"{player1} wins the game!")
        elif player2_wins > player1_wins:
            print(f"{player2} wins the game!")
        else:
            print("The game is a tie!")

if __name__ == "__main__":
    dice_rolling_game()
