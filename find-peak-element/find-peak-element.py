class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
         
        L = 0
        R = len(nums) - 1
        
        
        
        while L < R:
            M = (L + R) // 2
            
            if nums[M] > nums[M + 1]:
                R = M
            else:
                L = M + 1
        return L
        