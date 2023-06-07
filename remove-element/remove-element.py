class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            
        j = 0
        
        for i in range(len(nums)):
            if nums[j] == val and nums[i] != val:  
                nums[j], nums[i] = nums[i], nums[j]
            
            if nums[j] != val:
                j += 1
        return j