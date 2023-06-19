class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        ans = [[1] * (n) for n in range(1, rowIndex + 2)]
        print(ans)
        for i in range(2, len(ans)): 
            for j in range(1, len(ans[i]) - 1):  
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        
        return ans[-1]