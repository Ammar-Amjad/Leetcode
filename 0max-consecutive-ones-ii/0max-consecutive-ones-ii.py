class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_seq = 0
        left = 0
        right = 0
        zeros = 0

        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            
            while zeros == 2:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            max_seq = max(max_seq, right - left + 1)

            right += 1

        return max_seq
        
        