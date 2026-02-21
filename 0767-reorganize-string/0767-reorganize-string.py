class Solution:
    def reorganizeString(self, s: str) -> str:
        
        n = len(s)
        s_cnt = Counter(s)
        max_freq = max(s_cnt.values())
        if max_freq > (n + 1) // 2:
            return ""

        h = [(-freq, ch) for ch, freq in s_cnt.items()]
        heapq.heapify(h)

        res = []
        while len(h) >= 2:
            f1, c1 = heapq.heappop(h)
            f2, c2 = heapq.heappop(h)

            res.append(c1)
            res.append(c2)

            f1 += 1
            f2 += 1

            if f1 != 0:
                heapq.heappush(h, (f1,c1))
            if f2 != 0:
                heapq.heappush(h, (f2,c2))

        if h:
            _, ch = heapq.heappop(h)
            res.append(ch)

        return "".join(res)

            