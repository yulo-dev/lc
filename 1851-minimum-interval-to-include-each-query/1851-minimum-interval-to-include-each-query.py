class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        
        intervals.sort()

        import heapq
        heap = []

        res = []
        i = 0

        ans = {}

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(heap, (end-start+1, end))
                i += 1

            while heap and heap[0][1] < q:
                 heapq.heappop(heap)

            ans[q] = heap[0][0] if heap else -1

        return [ans[q] for q in queries]