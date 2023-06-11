class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hlen = len(haystack)
        nlen = len(needle)
        
        for i in range(hlen - nlen + 1):
            for j in range(nlen):
                if haystack[i + j] != needle[j]:
                    break
                if j == nlen - 1:
                    return i

        return -1