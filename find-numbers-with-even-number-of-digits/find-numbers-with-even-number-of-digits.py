class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evenc = 0
        
        for n in nums: 
            c = 0
            
            while n:
                n = n // 10
                c += 1
            
            if c % 2 == 0:
                evenc += 1
        
        return evenc