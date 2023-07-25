 

class Solution:
    def minDifficulty(self, jobD: List[int], d: int) -> int:
        if len(jobD) < d:
            return -1
        @cache
        def dfs(i, RemD):
            if RemD == 1:
                return max(jobD[i:])
            else:
                val = []
                for j in range(i, len(jobD) - RemD + 1):
                    val += [max(jobD[i: j +1]) + dfs(j + 1, RemD - 1)]
                return min(val)
        
        return dfs(0, d)
