class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
         
        dic = {}
        
        for i in range(len(nums1)):
            if nums1[i] in dic:
                dic[nums1[i]] += 1
            else:
                dic[nums1[i]] = 1
        res = []
        
        for i in range(len(nums2)):
            if nums2[i] in dic:
                dic[nums2[i]] -= 1
                res.append(nums2[i])
                if dic[nums2[i]] == 0:
                    del dic[nums2[i]]
        return res
        
        
        