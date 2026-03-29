class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows=[set() for _ in range(n)]
        cols=[set() for _ in range(n)]
        squars=[set() for _ in range(n)]

        for r in range(n):
            for c in range(n):

                value= board[r][c]
                box_index= (r // 3) * 3 + (c // 3)

                if value == ".":
                    continue
                
                if (value in rows[r] or
                    value in cols[c] or 
                    value in squars[box_index]):
                    return False

                rows[r].add(value)
                cols[c].add(value)
                squars[box_index].add(value)
        return True
