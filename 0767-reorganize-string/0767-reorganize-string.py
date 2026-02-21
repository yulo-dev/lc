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


        #這邊可以這樣寫 是因為前面先做了這個可行性判斷：
        #if maxFreq > (n + 1) // 2: return ""
        #這個判斷保證：最多的字母不會多到需要在最後留下 2 個以上還沒放。
        #因此最後 heap 裡如果還剩一個元素，它的頻率一定只會剩 1（也就是 freq == -1）

        #為什麼最後不可能剩 2 以上？
        #因為主迴圈每次都拿兩個不同字母放進 res（用掉 2 個字元），會把高頻字母一直往下消耗、並且逼它跟別的字母交錯。
        #若某字母最後還能剩 2 個，代表它「一直找不到其他字母來隔開它」，那本質上就會違反可行條件 maxFreq <= (n+1)//2。
        if h:
            _, ch = heapq.heappop(h)
            res.append(ch)

        return "".join(res)

            