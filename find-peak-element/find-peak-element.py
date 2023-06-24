class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        L = 0
        R = len(nums) - 1
        
        while L <= R:
            M = (L + R) // 2
            if M - 1 >= 0 and M + 1 < len(nums):
                if nums[M - 1] < nums[M] > nums[M + 1]:
                    return M
                elif nums[M - 1] < nums[M] < nums[M + 1]:
                    L = M + 1
                elif nums[M - 1] > nums[M] > nums[M + 1]:
                    R = M - 1
                else:
                    R = M - 1
            elif M - 1 >= 0:
                if nums[M - 1] > nums[M]:
                    return M - 1
                else:
                    return M
            elif M + 1 < len(nums):
                if nums[M] < nums[M + 1]:
                    return M + 1
                else:
                    return M

        return -1