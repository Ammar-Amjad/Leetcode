class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = -1
        for n in nums:
            cur = abs(n)
            
            if nums[cur] < 0:
                dup = cur
                break
            nums[cur] = -nums[cur]
            
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        return dup