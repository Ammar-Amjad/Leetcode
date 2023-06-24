class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        def FindX(arr, X):
            L = 0
            R = len(arr) - 1

            while L <= R:
                M = (L + R) // 2

                if arr[M] == X:
                    return M
                elif arr[M] < X:
                    L = M + 1
                elif arr[M] > X:
                    R = M - 1
            return R
        idx = FindX(arr, x)
         
        L = idx
        R = idx + 1
        res = [] 
        while len(res) != k:
            if L >= 0 and R < len(arr):
                if abs(arr[L] - x) <= abs(arr[R] - x):
                    res.append(arr[L])
                    L -= 1
                else:
                    res.append(arr[R])
                    R += 1
            elif L < 0:
                res.append(arr[R])
                R += 1
                
            elif R >= len(arr):
                res.append(arr[L])
                L -= 1

        return sorted(res)
        