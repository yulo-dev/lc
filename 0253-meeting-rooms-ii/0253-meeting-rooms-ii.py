class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:

        intervals.sort()

        room = len(intervals)

        import heapq
        heap = []
        
        for start, end in intervals:
            if heap and heap[0] <= start:
                room -= 1
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
        
        return room
