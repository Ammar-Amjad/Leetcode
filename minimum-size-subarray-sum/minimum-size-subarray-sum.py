class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minL = float('inf')
        left = 0
        Sum = 0
        
        for P in range(len(nums)):
            Sum += nums[P]
            while Sum >= target:
                minL = min(minL, P - left + 1)
                Sum -= nums[left]
                left += 1
             
        return minL if minL != float('inf') else 0
      