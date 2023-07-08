class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(par, l, r): 
            
            if len(par) == (n * 2):
                res.append(par)
                return 
            if l + 1 <= n:
                dfs(par + '(', l + 1, r)
            if r + 1 <= l:            
                dfs(par + ')', l, r + 1)
            return 
        
        dfs("", 0, 0)
        
        return res