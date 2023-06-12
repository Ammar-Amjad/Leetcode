class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums2) < len(nums1):
            return self.intersect(nums2, nums1)
        
        dic = {}
        for i in range(len(nums1)):
            if nums1[i] in dic:
                dic[nums1[i]] += 1
            else:
                dic[nums1[i]] = 1
         
        k = 0
        for i in range(len(nums2)):
            if nums2[i] in dic:
                dic[nums2[i]] -= 1
                nums1[k] = nums2[i]
                k += 1
                if dic[nums2[i]] == 0:
                    del dic[nums2[i]]
        return nums1[:k]
        
        
        