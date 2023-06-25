class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def BS(nums, target):
            
            L = 0
            R = len(nums) - 1
            
            while L <= R:
                M = (L + R) // 2
                if nums[M] == target:
                    return nums[M]
                elif nums[M] < target:
                    L = M + 1
                elif nums[M] > target:
                    R = M - 1
                print(L, R)
            return -1
            
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        res = []
        for n2 in nums2:
            val = BS(nums1, n2)
            
            if val not in res and val != -1:
                res.append(val)
            
        return res