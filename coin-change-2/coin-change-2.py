class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        prev_row = [0 for i in range(amount + 1)]

        for row in range(len(coins) - 1, -1, -1):
            curr_row = [0 for i in range(amount + 1)]
            
            for col in range(amount + 1):
                if col == 0:
                    curr_row[col] = 1
                else:    
                    if col - coins[row] >= 0:
                        curr_row[col] += curr_row[col - coins[row]]

                    if row + 1 < len(coins):
                        curr_row[col] += prev_row[col]
                    
            prev_row = curr_row
            
                
        return prev_row[amount]
                    