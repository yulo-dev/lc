class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        import heapq
        heap = []

        for i in range(len(matrix)):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        cnt = 0
        while heap:
            num, i, j = heapq.heappop(heap)
            cnt += 1
            if cnt == k:
                return num

            if j+1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))