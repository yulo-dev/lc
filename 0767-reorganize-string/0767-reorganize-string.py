class Solution:
    def reorganizeString(self, s: str) -> str:
        
        s_cnt = Counter(s)

        if max(s_cnt.values()) > (len(s) + 1) // 2:
            return ""

        max_heap = []
        for ch, freq in s_cnt.items():
            heapq.heappush(max_heap, (-freq, ch))


        res = []
        used_freq = 0
        used_ch = ""

        while max_heap:
            freq, ch = heapq.heappop(max_heap)
            res.append(ch)
            freq += 1

            if used_freq < 0:
                heapq.heappush(max_heap, (used_freq, used_ch))

            used_freq = freq
            used_ch = ch

        return "".join(res)