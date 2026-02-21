class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        h = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(h, (nums1[i] + nums2[0], i, 0))

        res = []
        while h and len(res) < k:
            _,i,j = heapq.heappop(h)
            res.append([nums1[i], nums2[j]])

            if j+1 < len(nums2):
                heapq.heappush(h, (nums1[i] + nums2[j+1], i, j+1))

        return res
