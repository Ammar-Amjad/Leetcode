def minRSA(nums):
    L = 0
    R = len(nums) - 1
    N = len(nums)
    
    while L <= R:
        M = (L + R) // 2
        
        if nums[M] <= nums[(M - 1 + N) % N] and nums[M] <= nums[(M + 1) % N]:
            return M
        elif nums[M] <= nums[R]:
            R = (M - 1 + N) % N
        elif nums[M] >= nums[L]:
            L = (M + 1) % N
        
    return L

def BS(nums, L, R, target):
    while L <= R:
        M = (L + R) // 2
        if nums[M] == target:
            return M
        elif target < nums[M]:
            R = M - 1
        else:
            L = M + 1
    return -1
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minIdx = minRSA(nums)
        print(minIdx)
        LR = BS(nums, 0, minIdx - 1, target)
        RR = BS(nums, minIdx, len(nums) - 1, target) 
        
        if LR != -1:
            return LR
        elif RR != -1:
            return RR
        else:
            return -1
        
        