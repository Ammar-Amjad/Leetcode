class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        mapping = { '}' : '{', ')' : '(', ']' : '[' }
        
        stack = []
        for i in range(len(s)):
            if s[i] in mapping and stack:
                val = stack.pop()
                if val != mapping[s[i]]:
                    return False
            else:
                stack.append(s[i])
        return not stack
        