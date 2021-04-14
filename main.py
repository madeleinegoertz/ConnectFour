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
      #print("Placed in r = {} c = {}".format(r, col))
    #print(placed)
    r = r - 1

  if not placed:
    print("Invalid input! This columns is full.")
    col = get_move(board, player)
  return board

# returns True if col is valid column
def is_valid_col(col):
  return col > 0 and col <= N_COLS

# returns True if player won, False if not
def has_won(board, player):
  return row_won(board, player) or col_won(board, player)or left_diag_won(board, player) or right_diag_won(board, player) 

# Looks for this shape
# ****
def row_won(board, player):
  row_won = False
  # loop through rows
  r = 0
  while r < N_ROWS and not row_won:
    # loop through cols in row
    # track count of consecutive symbol
    c = 0
    num_consecutive = 0
    while c < N_COLS and not row_won:
      if board[r][c] == player:
        num_consecutive += 1
      else:
        num_consecutive = 0
      row_won = num_consecutive >= 4
      c += 1
    r += 1
  return row_won

# Looks for this shape
# *
# *
# *
# *
def col_won(board, player):
  col_won = False
  # loop through cols
  c = 0
  while c < N_COLS and not col_won:
    # loop through rows in col
    # track count of consecutive symbol
    r = 0
    num_consecutive = 0
    while r < N_ROWS and not col_won:
      if board[r][c] == player:
        num_consecutive += 1
      else:
        num_consecutive = 0
      col_won = num_consecutive >= 4
      r += 1
    c += 1
  return col_won

# Looks for this shape
# *
#  *
#   *
#    *
def left_diag_won(board, player):
  diag_won = False
  # loop through rows (0 to 5) and columns (0 to 6)
  r = 0
  i = 0
  while r < N_ROWS and not diag_won:
    c = 0
    num_consecutive = 0
    while c < N_COLS and r < N_ROWS and not diag_won:
      if board[r][c] == player:
        num_consecutive += 1
        #print("a - r = {}, c = {}, nc = {}".format(r, c, num_consecutive))
      else:
        num_consecutive = 0
      diag_won = num_consecutive >= 4
      r += 1
      c += 1
    i += 1
    r = i
  # loop through columns (1 to 6) and rows (0 to 5)
  c = 1
  i = c
  while c < N_COLS and not diag_won:
    r = 0
    num_consecutive = 0
    while r < N_ROWS and c < N_COLS and not diag_won:
      if board[r][c] == player:
        num_consecutive += 1
        #print("b - r = {}, c = {}, nc = {}".format(r, c, num_consecutive))
      else:
        num_consecutive = 0
      diag_won = num_consecutive >= 4
      r += 1
      c += 1
    #print(i)
    i += 1
    c = i
  return diag_won

# Looks for this shape
#    *
#   *
#  *
# *
def right_diag_won(board, player):
  diag_won = False
  # First loop through rows (5 to 0) then columns (0 to 6)
  r = N_ROWS - 1
  i = 0
  while r >= 0 and not diag_won:
    c = 0
    num_consecutive = 0
    while c < N_COLS and r >= 0 and not diag_won:
      if board[r][c] == player:
        num_consecutive += 1
        #print("a - r = {}, c = {}, nc = {}".format(r, c, num_consecutive))
      else:
        num_consecutive = 0
      diag_won = num_consecutive >= 4
      r -= 1
      c += 1
    i += 1
    r = N_ROWS - 1 - i
  # Then loop through columns (1 to 6) then rows (5 to 0)
  c = 1
  i = c
  while c < N_COLS and not diag_won:
    r = N_ROWS - 1
    num_consecutive = 0
    while r >= 0 and c < N_COLS and not diag_won:
      if board[r][c] == player:
        num_consecutive += 1
        #print("b - r = {}, c = {}, nc = {}".format(r, c, num_consecutive))
      else:
        num_consecutive = 0
      diag_won = num_consecutive >= 4
      r -= 1
      c += 1
    i += 1
    c = i
  #print(diag_won)
  return diag_won
        

def main():
  player = "x"
  board = initialize()
  game_won = False
  max_turns = N_ROWS * N_COLS
  turn = 1

  while not game_won and turn <= max_turns:
    print_board(board)
    col = get_move(board, player)
    board = make_move(board, player, col)
    game_won = has_won(board, player)
    player = "o" if player == "x" else "x" # switch player
    turn += 1
  
  print_board(board)
  if not game_won: # game ended but nobody won
    print("Tie game.")
  else:
    print("Player {} wins!".format("o" if player == "x" else "x"))

main()