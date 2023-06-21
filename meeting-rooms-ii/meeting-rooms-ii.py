class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort()
        for i in range(len(intervals)):
            if len(heap) == 0:
                heapq.heappush(heap, intervals[i][1])
            elif heap[0] < intervals[i][1]:
                if intervals[i][0] >= heap[0]:
                    heapq.heappop(heap)
                heapq.heappush(heap, intervals[i][1])
            else:
                heapq.heappush(heap, intervals[i][1])
        print(heap[0])
        return len(heap)
