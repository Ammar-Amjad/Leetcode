class Solution:
    @cache
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        return ((self.numTilings(n - 1) * 2) + self.numTilings(n - 3)) % (10**9 + 7)
        