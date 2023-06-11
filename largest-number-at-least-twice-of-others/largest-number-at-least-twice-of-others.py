class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        maxN = 0
        maxi = -1
        for i in range(len(nums)):
            if nums[i] > maxN:
                maxi = i
                maxN = nums[i]
        
        for i in range(len(nums)):
            if (nums[i] * 2) > maxN and i != maxi:
                return -1
        return maxi