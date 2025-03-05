#Make a Rock Paper Scissors game. Have each user enter their name
# and their choice (rock, paper, or scissors). 
# Rock beats scissors 
# Scissors beats paper 
# Paper beats rock 


user1_answer = input(" Player 1 do you want to choose rock, paper or scissors?" )
user2_answer = input(" Player 2 do you want to choose rock, paper or scissors?" )

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")

print(compare(user1_answer, user2_answer))



# Make a Tic Tac Toe game. There are many solutions to this problem,
#this just one of them. Use your own methods to think through it rather than
# trying to understand this one. 
# Break it into steps: 
# Print board 
# Alternate between x and O
# Hold the X and O position for all board slots
# Ask user to enter position
# Determine position on board 
# Update board slots 
# Break it into small steps and functions 


# Function to print the board
def print_board(board):
    for row in board:
        print(" | ", row[0], " | ", row[1], " | ", row[2], " | ")
        print("-------------")

# Function to check for a winner
def check_winner(board, player):
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to check if the board is full
def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))
        
        if board[row][col] != " ":
            print("Cell is already taken, try again.")
            continue
        
        board[row][col] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()