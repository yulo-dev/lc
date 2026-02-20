class Solution:
    def frequencySort(self, s: str) -> str:
        s_cnt = Counter(s)
        h = []

        for ch, freq in s_cnt.items():
            heapq.heappush(h, (-freq, ch))

        # 依序取出並組合成字串
        res = []
        while h:
            neg_freq, ch = heapq.heappop(h)
            res.append(ch * (-neg_freq)) # 負負得正，還原頻率
        
        return "".join(res)