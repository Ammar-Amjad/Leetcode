class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        Mid = int(len(nums) / 2) 
        
        left_list = self.sortArray(nums[:Mid])
        right_list = self.sortArray(nums[Mid:])
        return merge(left_list, right_list)
    
    def merge(left_list, right_list):
        lp = 0
        rp = 0
        res = []
        while lp < len(left_list) and rp < len(right_list):
            if left_list[lp] <= right_list[rp]:
                res.append(left_list[lp])
            else:
                res.append(right_list[rp])
        
        res.extends(left_list[lp:])
        res.extends(right_list[rp:])
        
        return res
        
        