class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        L = 0
        R = len(letters) - 1
        res = letters[0]

        while L <= R:
            M = (L + R) // 2
            
            if letters[M] == target:
                L = M + 1
            elif letters[M] < target:
                L = M + 1
            elif letters[M] > target:
                res = letters[M]
                R = M - 1
        
        return res