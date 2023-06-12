class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()

        i = 0
        j = 0

        k = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                nums1[k] = nums1[i]
                k += 1
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return nums1[:k]
        
        
        
        