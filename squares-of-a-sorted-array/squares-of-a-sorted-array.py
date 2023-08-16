class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        N = len(nums)
        
        res = [0 for _ in range(N)]
        
        p1 = 0
        p2 = N - 1
        
        i = N - 1
        
        while p2 >= p1:
            prod1 = nums[p1] * nums[p1]
            prod2 = nums[p2] * nums[p2]
            if prod1 > prod2:
                res[i] = prod1
                p1 += 1
            else:
                res[i] = prod2
                p2 -= 1 
            i -= 1
        
        return res