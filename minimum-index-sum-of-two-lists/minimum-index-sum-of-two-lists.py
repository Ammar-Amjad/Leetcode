class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map1 = {}
        
        for i in range(len(list1)):
            map1[list1[i]] = i
        
        minRes = float('inf')
        res = 0
        resList = []
        for i in range(len(list2)):
            if list2[i] in map1:            
                res = map1[list2[i]] + i 
                if res < minRes:
                    minRes = res
                    resList = [list2[i]]
                elif res == minRes:
                    resList.append(list2[i]) 
        return resList