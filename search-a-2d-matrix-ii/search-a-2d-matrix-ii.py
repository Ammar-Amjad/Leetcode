class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        r = 0
        c = cols -1
        p = matrix[r][c]
        
        while 0 <= r < rows and 0 <= c < cols:
            if matrix[r][c] == target:
                return True
            elif target < matrix[r][c]:
                c -= 1
            else:
                r += 1
        return False
        