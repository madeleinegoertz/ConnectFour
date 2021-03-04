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

# returns true if the player passed in has won, false if not. 
def has_won(board, player):
  return row_won(board, player) or col_won(board, player) or left_diag_won(board, player)   or right_diag_won(board, player)

# return True if that player has 4 in a row across. 
# Looks like this
# xxxx
def row_won(board, player):
  has_won = False
  r = 0
  while r < N_ROWS and not has_won:
    c = 0
    num_consecutive = 0
    while c < N_COLS and not has_won:
      if board[r][c] == player:
        num_consecutive += 1
        print("r = {}, c= {}, n = {}".format(r, c, num_consecutive))
      else:
        num_consecutive = 0
      has_won = num_consecutive >= 4
      c += 1
    r += 1
  return has_won

# x
# x
# x
# x
def col_won(board, player):
  return False

# x
#  x
#   x
#    x
def left_diag_won(board, player):
  return False

#    x
#   x
#  x
# x
def right_diag_won(board, player):
  return False


def main():
  player = "x"
  board = initialize()
  has_won_game = False
  turn = 1

  # main game loop elapses if someone wins or the board fills up
  while not has_won_game and turn <= N_ROWS * N_COLS:
    print_board(board)
    col = get_move(board, player)
    board = make_move(board, player, col)
    has_won_game = has_won(board, player)
    player = "o" if player == "x" else "x" # switch player
    turn += 1
  
  print_board(board)
  if not has_won_game: # if the game is over but no one won. 
    print("Tie game.")
  else:
    print("Player {} wins!".format("o" if player == "x" else "x"))

main()