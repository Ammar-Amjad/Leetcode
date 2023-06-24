class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        L = 0
        R = len(nums) - 1
        
        while L <= R:
            M = (L + R) // 2 
            if M == 0:
                if nums[M] > nums[M + 1]:
                    return M
                else:
                    return M + 1
                
            elif M == len(nums) - 1:
                if nums[M - 1] < nums[M]:
                    return M
                else:
                    return M - 1
                
            else:
                if nums[M - 1] < nums[M] > nums[M + 1]:
                    return M
                elif nums[M - 1] < nums[M] < nums[M + 1]:
                    L = M + 1
                elif nums[M - 1] > nums[M] > nums[M + 1]:
                    R = M - 1
                else:
                    L = M + 1
                
            
        return -1