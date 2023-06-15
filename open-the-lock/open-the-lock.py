class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def neighbors(comb):
            res = set()
            for i in range(4):
                x = int(comb[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield comb[:i] + str(y) + comb[i + 1:]

        queue = deque([('0000', 0)])
        seen = {'0000'}
        dead = set(deadends)

        while queue:
            comb, depth = queue.popleft()
            if comb == target:
                return depth
            if comb in dead:
                continue
            for nei in neighbors(comb):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth + 1)) 
        return -1