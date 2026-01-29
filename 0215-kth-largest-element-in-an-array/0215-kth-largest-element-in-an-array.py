class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for x in nums:
            heapq.heappush(h, x)
            if len(h) > k: #一路維持h裡面有k個元素
                heapq.heappop(h) #如果超過k個元素就踢掉最小的, 所以裡面剩下的是一路篩選完較大的k個
        return h[0] #因為 heap 裡維持的是「全局最大的 k 個」，其中最小的那個就是第 k 大


        #time: O(nlogk), 因為heappush & heappop 最多是O(logk) 然後有n個元素
        #space: O(k) 因為h最多只存 k 個元素