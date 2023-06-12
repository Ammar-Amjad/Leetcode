class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        
        for i in range(len(numbers)):
            n = numbers[i]
            if n not in dic:
                dic[target - n] = i + 1
            else:
                return [dic[n], i + 1]