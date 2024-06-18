import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "player"
    else:
        return "computer"

def play_round():
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    winner = get_winner(player_choice, computer_choice)
    
    if winner == "tie":
        print("It's a tie!\n")
    elif winner == "player":
        print("You win this round!\n")
    else:
        print("Computer wins this round!\n")
    
    return winner

def rock_paper_scissors():
    player_wins = 0
    computer_wins = 0
    rounds = 3
    
    for i in range(rounds):
        print(f"Round {i+1}:")
        winner = play_round()
        
        if winner == "player":
            player_wins += 1
        elif winner == "computer":
            computer_wins += 1
        
        if player_wins == 2:
            print("You win the game!")
            break
        elif computer_wins == 2:
            print("Computer wins the game!")
            break
    
    if player_wins < 2 and computer_wins < 2:
        if player_wins > computer_wins:
            print("You win the game!")
        elif computer_wins > player_wins:
            print("Computer wins the game!")
        else:
            print("The game is a tie!")

if __name__ == "__main__":
    rock_paper_scissors()
