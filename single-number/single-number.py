class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        Sum = 0
        dic = {}
        
        for n in nums:
            if n in dic:
                dic[n] += 1
                res += (2 * n)
            else:
                dic[n] = 1
            Sum += n
        
        return Sum - res