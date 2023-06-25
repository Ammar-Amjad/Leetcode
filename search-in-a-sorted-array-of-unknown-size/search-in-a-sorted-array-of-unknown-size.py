# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:
def BS(reader, L, R, target):
    while L <= R:
        M = (L + R) // 2
        val = reader.get(M)
        if val == target:
            return M
        elif val < target:
            L = M + 1
        elif val > target:
            R = M - 1
    return -1


class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        L = 0
        R = 1
        while reader.get(R) < target:
            L = R
            R = R * 2
        
        return BS(reader, L, R, target)
        