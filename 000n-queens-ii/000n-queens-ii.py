class Solution:
    def totalNQueens(self, n: int) -> int:
        
        res = []
        board = [["."] * n for _ in range(n)]
        
        cols = set()
        posDiag = set()
        negDiag = set()
        
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'
        
        backtrack(0) 
        return len(res)