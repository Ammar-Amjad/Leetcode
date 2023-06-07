class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        hlist = [0] * 101
        for h in heights:
            hlist[h] += 1
        
        count = 0
        currh = 0
        
        for hi in range(len(heights)):
            while hlist[currh] == 0:
                currh += 1
            
            if currh != heights[hi]:
                count += 1
                
            hlist[currh] -= 1
        return count