   
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        
        if l1 + l2 < l3:
            return False
        @cache
        def dfs(i, j, k):
            
            if i == l1  and j == l2  and k == l3 :
                return True
            elif k == l3:
                return False
            
            v = False
            if i < l1 and s1[i] == s3[k]:
                v = v or dfs(i + 1, j, k + 1)
            if j < l2 and s2[j] == s3[k]:
                v = v or dfs(i, j + 1, k + 1)
            return v
            
        
        return dfs(0, 0, 0)