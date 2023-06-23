class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def LBS(Nums, target):
            L = 0
            R = len(Nums) - 1
            res = -1 
            
            while L <= R:
                M = (L + R) // 2
                
                if target == Nums[M]:
                    res = M
                    R = M - 1
                elif target < Nums[M]:
                    R = M - 1
                else:
                    L = M + 1
            return res
        
        def RBS(Nums, target):
            L = 0
            R = len(nums) - 1
            res = -1
            
            while L <= R:
                M = (L + R) // 2
                
                if target == Nums[M]:
                    res = M
                    L = M + 1
                elif target < Nums[M]:
                    R = M - 1
                else:
                    L = M + 1
            return res
        
        return [LBS(nums, target), RBS(nums, target)]