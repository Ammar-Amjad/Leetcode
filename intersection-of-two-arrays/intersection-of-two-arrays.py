class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Set1 = set()
        Set2 = set()
        
        for n in nums1:
            if n not in Set1:
                Set1.add(n)
        
        for n in nums2:
            if n not in Set2:
                Set2.add(n)
        
        Set3 = set()
        
        for n in Set1:
            if n in Set2:
                Set3.add(n)
        return Set3
        