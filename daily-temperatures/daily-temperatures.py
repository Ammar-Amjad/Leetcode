class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        stack = []
        ans = [0] * n
        
        for curr_day, curr_temp in enumerate(temps):
            while stack:
                if stack[-1][0] < curr_temp:
                    prev_temp, prev_day = stack.pop()        
                    ans[prev_day] = curr_day - prev_day
                else:
                    break
            stack.append([curr_temp, curr_day])
        return ans    
        
                
            