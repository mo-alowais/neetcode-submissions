from functools import reduce
import operator
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        transpose = zip(*board)
        for i in board:
            i = list(filter(lambda x: x.isnumeric(), i))
            if len(set(i)) != len(i): return False

        for i in transpose:
            i = list(filter(lambda x: x.isnumeric(), i))
            if len(set(i)) != len(i): return False
        

        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                boardslice = list(x[j:j+3] for x in board[i:i+3])
                square = reduce(operator.add, boardslice, []) # flatten
                square = list(filter(lambda x: x.isnumeric(),square))
    
                if len(set(square)) != len(square): return False
        return True
        