class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        def CRD(mid):
            visited = [[False for c in range(col)] for _ in range(row)]
            queue = [(0, 0)]

            while queue:
                x, y = queue.pop(0)
                if x == row - 1 and y == col - 1:
                    return True
                
                visited[x][y] = True

                for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    newx = x + dx
                    newy = y + dy

                    if 0 <= newx < row and 0 <= newy < col and not visited[newx][newy]:
                        current_diff = abs(heights[newx][newy] - heights[x][y])

                        if current_diff <= mid:
                            visited[newx][newy] = True
                            queue.append((newx, newy))

        L = 0
        R = 10**6
        ans = 10**6

        while L <= R:
            mid = (L + R) // 2
            if CRD(mid):
                R = mid - 1
                ans = mid
            else:
                L = mid + 1
        return ans