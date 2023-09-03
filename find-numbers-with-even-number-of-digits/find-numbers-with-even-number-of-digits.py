class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums: 
            if (floor(math.log10(n)) + 1) % 2 == 0:
                count += 1
                
        return count
            