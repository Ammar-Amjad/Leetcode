class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums: 
            temp = n
            digits = 0
            
            while temp:
                temp = temp // 10
                digits += 1
                
            if digits % 2 == 0:
                count += 1
            
            # if (floor(math.log10(n)) + 1) % 2 == 0:
                # count += 1
                
        return count
            