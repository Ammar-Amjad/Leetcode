class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        L = list()
        Lp = 0
        Rp = len(nums) - 1
        
        while Lp <= Rp:
            Lv = abs(nums[Lp])
            Rv = abs(nums[Rp])
            
            if Lv < Rv:
                L.append(Rv ** 2)
                Rp -= 1
            else:
                L.append(Lv ** 2)
                Lp += 1
        return L[::-1]
            