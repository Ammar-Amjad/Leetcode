class Solution:
    def binarySearch(self, row):
        L = 0
        R = len(row)

        while L < R:
            Mid = (L + R) // 2 

            if row[Mid] == 1:
                L = Mid + 1
            else:
                R = Mid

        return L        

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        heap = [] 

        for i in range(len(mat)):
            soliders = self.binarySearch(mat[i])
            entry = (-1 * soliders, -1 * i)
            if len(heap) < k or entry > heap[0]:
                heapq.heappush(heap, entry) 
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        while heap:
            soliders, i = heapq.heappop(heap)
            ans.append(-1 * i)

        return ans[::-1]








