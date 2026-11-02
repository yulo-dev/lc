class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        
        import heapq
        heap = []

        for i in range(len(nums1)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        res = []
        while heap and len(res) < k:
            min_sum, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            if j+1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))

        return res