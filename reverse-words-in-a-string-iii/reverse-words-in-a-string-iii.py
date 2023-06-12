class Solution:
    def reverseWords(self, s: str) -> str:
        l = 0
        r = 0
        res = ''
        s += ' '

        while r < len(s):
            if s[r] != ' ':
                r += 1
            elif s[r] == ' ':
                res += s[l: r + 1][::-1]
                r += 1
                l = r
        
        return res[1:] 