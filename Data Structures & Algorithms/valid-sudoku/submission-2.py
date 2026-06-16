from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rl = len(board)
        cl = len(board[0])

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)

        for r in range(rl):
            for c in range(cl):
                num = board[r][c]
                row = r//3
                col = c//3
                box_num = (row,col)
                if num == ".":
                    continue
                if num in rows[r] or num in cols[c] or num in boxs[box_num]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                boxs[box_num].add(num)

        return True 
