def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal wins
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical wins
        [0, 4, 8], [2, 4, 6]              # Diagonal wins
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw(board):
    return all(space in ['X', 'O'] for space in board)

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    player1 = input("Enter the name of Player 1 (X): ")
    player2 = input("Enter the name of Player 2 (O): ")
    players = [(player1, 'X'), (player2, 'O')]
    current_player = 0
    
    print_board(board)
    
    while True:
        player_name, player_symbol = players[current_player]
        move = int(input(f"{player_name}'s turn ({player_symbol}). Enter a position (1-9): ")) - 1
        
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        
        board[move] = player_symbol
        print_board(board)
        
        if check_winner(board, player_symbol):
            print(f"Congratulations {player_name}! You have won the game.")
            break
        
        if is_draw(board):
            print("It's a draw!")
            break
        
        current_player = 1 - current_player

if __name__ == "__main__":
    tic_tac_toe()
