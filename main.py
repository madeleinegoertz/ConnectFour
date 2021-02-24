N_ROWS = 6
N_COLS = 7

def initialize():
  board = [["."] * N_COLS for i in range(N_ROWS)]
  return board

# TODO: allow for more than 9 columns
def print_board(board):
  text = ""
  for i in range(N_COLS):
    text += str(i+1) + " "
  print(text)
  print("-" * (2 * N_COLS - 1))
  for row in board:
    print("|".join(row))

# input player move from console
def get_move(board, player):
  col = int(input("Player {} enter a column:".format(player)))
  # check if the column is valid
  if not is_valid_col(col):
    print("Invalid input! Please enter a column between 1 and {}".format(N_COLS))
    col = get_move(board, player)
  
  # zero index column 
  col = col - 1
  return col

def make_move(board, player, col):
  placed = False
  r = len(board) - 1
  while not placed and r >= 0:
    if board[r][col] == ".":
      board[r][col] = player
      placed = True
    #print(placed)
    r = r - 1

  if not placed:
    print("Invalid input! This columns is full.")
    col = get_move(board, player)
  return board

# returns True if col is valid column
def is_valid_col(col):
  return col > 0 and col <= N_COLS

def has_won(board): # returns string of winning player or empty string, or "Tie"
  return ""

def main():
  player = "x"
  board = initialize()
  winner = has_won(board)

  while winner == "":
    print_board(board)
    col = get_move(board, player)
    board = make_move(board, player, col)
    winner = has_won(board)
    player = "o" if player == "x" else "x" # switch player
  
  print_board(board)
  if winner == "Tie":
    print("Tie game.")
  else:
    print("Player {} wins!".format(winner))

main()