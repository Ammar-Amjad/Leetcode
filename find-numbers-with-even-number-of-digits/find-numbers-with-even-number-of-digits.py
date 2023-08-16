class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evenc = 0
        
        for n in nums: 
            c = math.floor(math.log10(n)) + 1
            
            if c % 2 == 0:
                evenc += 1
        
        return evenc