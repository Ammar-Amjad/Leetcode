class Solution:
    def numSquares(self, n: int) -> int:
        
        sq_nums = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]

        level = 0
        queue = {n}
        while queue:
            level += 1
            next_queue = set()
            for rem in queue:
                for sq_num in sq_nums:
                    if rem == sq_num:
                        return level
                    elif rem < sq_num:
                        break
                    else:
                        next_queue.add(rem - sq_num)
            queue = next_queue
        return level