class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        
        while L < R:
            M = (L + R) // 2
            
            if nums[M] < nums[R]:
                R = M
            else:
                L = M + 1
        return nums[L]