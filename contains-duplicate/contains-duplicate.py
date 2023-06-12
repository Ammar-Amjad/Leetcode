class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Set = set()
        for i in range(len(nums)):
            if nums[i] in Set:
                return True
            else:
                Set.add(nums[i])
        return False