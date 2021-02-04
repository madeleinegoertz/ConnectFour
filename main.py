N_ROWS = 6
N_COLS = 7


# sets up empty board
def init():
  return [["o" for i in range(N_COLS)] for j in range(N_ROWS)]


# print out a correctly formatted board
def print_board(board):
  print("1 2 3 4 5 6 7")
  print(" " * (2 * N_COLS - 1))
  for row in board:
    print("|".join(row))

# Ask player to input col and validate
def get_move(board, player):
  col = int(input("Player {} enter a column:".format(player)))
  # check if col is valid
  if (col < 1 or col > N_COLS):
    print("Invalid input. Enter a number in range.")
    col = get_move(board, player)
  
  #convert from indexing by 0 to indexing by 1
  col -= 1

  #  check if column is full
  col_full = True
  for i in range(N_ROWS):
    if board[i][col] == "O":
      col_full = False
      break
  if col_full:
    print("That column is full.  Please try again.")
    col = get_move(board, player)
  return col



# places the piece in the correct col
def make_move(board, player, col):
  row = 0
  for i in range(HEIGHT):
    if board[i][col] == "O":            row = i        else:            break    board[row][col] = player    return board


# return player that's won or an empty string
def check_win(board):
  pass


def main():
    board = init()
    player = "x"
    winner = ""

    while winner == "":
        print_board(board)
        col = get_move(board, player)
        make_move(board, player, col)
        winner = check_win(board)
        if player == "x":
            player = "o"
        else:
            player = "x"

    print_board(board)
    if winner == "Tie":
        print("Tie game.")
    else:
        print("Player {} wins!".format(winner))


if __name__ == "__main__":
  main()
