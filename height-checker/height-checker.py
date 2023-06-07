class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h2 = sorted(heights.copy())
        count = 0 
        for hi in range(len(h2)):
            if h2[hi] != heights[hi]:
                count += 1
        return count