class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        
        for n in nums:
            if n in dic:
                del dic[n]
            else:
                dic[n] = 1 
        for k, v in dic.items():
            if v == 1:
                return k 
        
        