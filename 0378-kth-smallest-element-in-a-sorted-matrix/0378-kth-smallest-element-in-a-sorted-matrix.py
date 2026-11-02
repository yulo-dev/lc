class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        import heapq
        heap = []

        for i in range(len(matrix)):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        while k > 0:
            ele, i, j = heapq.heappop(heap)

            if j + 1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))

            k -= 1

        return ele
