class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        cnt = Counter(tasks)
        
        # 2. 建立 Max-Heap：存儲「目前可執行」的任務頻率
        h = [-c for c in cnt.values()]
        heapq.heapify(h)

        # cooldown queue: (neg_remaining_count, ready_time)
        # 格式：(剩餘次數, 可以再次進入 Heap 的時間)
        cooldown = deque()

        time = 0
        # 只要還有任務沒做完 (Heap 有東西) 或還有任務在冷卻 (Queue 有東西)，就不停下
        while h or cooldown:
            time += 1

            # --- 執行階段 ---
            if h:
                # 從 Heap 拿出目前頻率最高的任務來做 (Greedy 策略)
                c = heapq.heappop(h) + 1  # +1 because c is negative => remaining-1
                if c != 0:
                    # 如果還沒做完，計算它「解凍」的時間點，丟進冷卻隊列
                    # 解凍時間 = 當前時間 + n
                    # 只有當 time 到達了它標註的 ready_time，它才能重獲自由回到 Heap
                    cooldown.append((c, time + n))


            # --- 恢復階段 ---
            # 檢查冷卻隊列的頭部，是否有任務已經「冷卻完成」？
            # move ALL tasks that are done cooling down back to heap
            while cooldown and cooldown[0][1] <= time:
                heapq.heappush(h, cooldown.popleft()[0])

        return time

        



#為了讓總時間最短，直覺告訴我們：出現頻率最高的任務要先做
#algo:Heap + Queue (冷卻名單)
#Max-Heap：儲存目前「可以執行」的任務（按頻率高低排）
#Queue：儲存正在「冷卻中」的任務。格式為 (剩餘頻率, 可以再次執行的時間)