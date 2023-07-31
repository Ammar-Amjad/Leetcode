class Solution:
    def numTilings(self, n: int) -> int:
        print(n)
        dp = [0 for _ in range(n + 1)]
        if n == 1:
            return 1
        back3 = 1
        if n == 2:
            return 2
        back2 = 2
        if n == 3:
            return 5
        back1 = 5
        
        for i in range(4, n + 1):
            back3, back2, back1 =  back2, back1, (back3 + (back1 * 2))
        return back1 % (10**9 + 7)
        