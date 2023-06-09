class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        List = []

        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                List.append(i)
        
        return List