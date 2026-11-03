class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        import heapq

        heap = []
        
        freq = defaultdict(int)

        for w in words:
            freq[w] += 1

        for w, num in freq.items():
            heapq.heappush(heap, (-num, w))

        res = []
        while k > 0:
            _, word = heapq.heappop(heap)
            res.append(word)
            k -= 1

        return res