class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L = 0
        R = len(nums) - 1
        
        while L <= R:
            M = (L + R) // 2
            val = nums[M]
            if val == target:
                return M
            elif val >= nums[L]:
                if target >= nums[L] and target < val:
                    R = M - 1
                else:
                    L = M + 1
            else:
                if target <= nums[R] and target > val:
                    L = M + 1
                else:
                    R = M - 1
        return -1