class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        prev_num = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] != prev_num: 
                prev_num = nums[i]
                count += 1
            
            if count == 3:
                return nums[i]
        
        return nums[0]