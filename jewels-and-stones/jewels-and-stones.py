class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        Set = set(jewels)
        JewelCount = 0
        
        for i in range(len(stones)):
            if stones[i] in Set:
                JewelCount += 1
        
        return JewelCount 