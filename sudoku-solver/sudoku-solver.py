class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        solved = False
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    b = (i // 3) * 3 + (j // 3)
                    
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[b].add(num)
        
        def backtrack(i, j):
            nonlocal solved
            if i == 9:
                solved = True
                return 
            
            new_i = i + (j + 1) // 9
            new_j = (j + 1) % 9
            
            if board[i][j] != '.':
                backtrack(new_i, new_j)
            else:
                for num in range(1, 10):
                    b = (i // 3) * 3 + (j // 3)
                    
                    if num not in rows[i] and num not in cols[j] and num not in boxes[b]:
                        rows[i].add(num)
                        cols[j].add(num)
                        boxes[b].add(num)
                        board[i][j] = str(num)
                        
                        backtrack(new_i, new_j)
                        
                        if not solved:
                            rows[i].remove(num)
                            cols[j].remove(num)
                            boxes[b].remove(num)
                            board[i][j] = '.'
            
        backtrack(0, 0)
        return board
                    