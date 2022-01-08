

from tictactoe import winner
import math
X = "X"
O = "O"
act=[[1,2],[1,4]]
EMPTY = None
board  = [[O, X, O],
          [X, X, X],
          [X, O,O]]

N=winner(board)
m=winner(board)
print(N)
print(m)
v=act[0]
print(v[0])
