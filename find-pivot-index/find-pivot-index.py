class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        Sum = sum(nums)
        leftSum = 0
        
        for i in range(len(nums)):
            if leftSum == (Sum - leftSum - nums[i]):
                return i
            leftSum += nums[i]
        return -1