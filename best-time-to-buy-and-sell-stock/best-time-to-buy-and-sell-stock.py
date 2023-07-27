class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      
        p1 = 0
        maxP = 0
        currP = 0
        
        for p2 in range(1, len(prices)):
            currP = prices[p2] - prices[p1]
            maxP = max(maxP, currP)
            
            if currP < 0:
                p1 = p2
            
        return maxP
            