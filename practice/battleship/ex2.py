board = []

for i in range(5):
  board.append(["O"] * 5)

def print_board(board_in):
  for row in board:
    print " ".join(row)
    
print_board(board)
