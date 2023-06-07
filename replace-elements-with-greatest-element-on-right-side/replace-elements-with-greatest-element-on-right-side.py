
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = -1
        maxSoFar = -1
        
        for i in range(len(arr) - 1, -1, -1):
            maxSoFar = max(maxSoFar, temp) 
            temp = arr[i] 
            arr[i] = maxSoFar 
        return arr