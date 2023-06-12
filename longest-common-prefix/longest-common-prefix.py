class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minL = float('inf')
        
        for s in strs:
            minL = min(len(s), minL)
        
        prefix = ''
        for i in range(minL):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return prefix
            prefix += c
        return prefix