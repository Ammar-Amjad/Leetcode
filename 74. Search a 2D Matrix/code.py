class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        
        L = 0
        R = (m * n) - 1
        print(matrix)
        while L <= R:
            M = (L + R) // 2

            ri = M // n
            ci = M % n 

            if matrix[ri][ci] == target: 
                return True
            elif matrix[ri][ci] > target:
                R = M - 1
            else:
                L = M + 1
        
        return False
