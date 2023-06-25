class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        l1 = len(nums1) 
        l2 = len(nums2) 
        
        half = (l1 + l2) // 2 
        L = 0
        R = l1 - 1 
            
        while True:
            
            M1 = (L + R) // 2
            M2 = half - M1 - 2
            n1l = nums1[M1] if M1 >= 0 else -float('inf')
            n1r = nums1[M1 + 1] if M1 + 1 < l1 else float('inf')
            n2l = nums2[M2] if M2 >= 0 else -float('inf')
            n2r = nums2[M2 + 1] if M2 + 1 < l2 else float('inf')
            
            if n1l <= n2r and n2l <= n1r:
                if (l1 + l2) % 2 == 0:
                    return (max(n1l, n2l) + min(n1r, n2r)) / 2
                else:
                    return min(n1r, n2r)
            elif n1l > n2r:
                R = M1 - 1
            else:
                L = M1 + 1
        