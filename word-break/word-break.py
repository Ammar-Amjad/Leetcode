class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        
        for i in range(len(dp)):
            if dp[i] != False:
                for word in words:
                    if i + len(word) < len(dp):                    
                        if word == s[i: i + len(word)]:                    
                            dp[i + len(word)] = True                
        
        return dp[len(s)]
        
        