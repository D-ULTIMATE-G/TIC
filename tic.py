#Function to print the Tic-Tac-Toe board
board = [[" " for _ in range(3)] for _ in range(3)]

def tic_tac_toe_board(board):
    for row in board:
       print("|".join(row))
       print("." * 5)
tic_tac_toe_board(board)
print("this is a tic_tac_toe board")
