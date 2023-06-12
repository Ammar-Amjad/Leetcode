class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = len(s) - 1

        while left <= right and s[left] == ' ':
            left += 1
        
        while left <= right and s[right] == ' ':
            right -= 1
        
        d = deque()
        word = []

        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        
        d.appendleft(''.join(word))
        return ' '.join(d)