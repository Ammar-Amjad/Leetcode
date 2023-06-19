class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def dfs(l, r):
            if l >= r:
                return 0
            
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            
            dfs(l + 1, r - 1)
        
        dfs(0, len(s) - 1)
        