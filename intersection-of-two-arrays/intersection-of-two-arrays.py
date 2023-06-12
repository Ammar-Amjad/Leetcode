class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dic = {}

        for n in nums1:
            dic[n] = dic[n] + 1 if n in dic else 1
        
        for n in nums2:
            if n in dic:
                del dic[n] 
                res.append(n)

        return res