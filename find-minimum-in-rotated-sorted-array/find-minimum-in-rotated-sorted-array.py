class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        N = len(nums)
        
        while L <= R:
            M = (L + R) // 2
            
            if nums[(M - 1 + N) % N] >= nums[M] <= nums[(M + 1) % N]:
                return nums[M]
            elif nums[M] <= nums[R]:
                R = (M - 1 + N) % N
            elif nums[M] >= nums[L]:
                L = (M + 1) % N
        return nums[L]
         