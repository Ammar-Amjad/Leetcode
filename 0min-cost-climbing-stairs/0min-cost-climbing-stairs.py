class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
         
        
        two_ahead = 0
        one_ahead = cost[len(cost) - 1] 
        
        for i in range(len(cost) - 2, -1, -1):
            curr = cost[i] + min(one_ahead, two_ahead)
            two_ahead = one_ahead
            one_ahead = curr
            
        return min(one_ahead, two_ahead) 