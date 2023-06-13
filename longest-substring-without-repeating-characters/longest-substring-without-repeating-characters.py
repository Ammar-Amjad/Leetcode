class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i = 0
        dic = {}
        mLen = 0
        P = 0
        
        while i < len(s):
            
            if s[i] in dic:
                P = max(dic[s[i]], P)
            
            
            mLen = max(mLen, i - P + 1)
            dic[s[i]] = i + 1
            i += 1
        
        return mLen