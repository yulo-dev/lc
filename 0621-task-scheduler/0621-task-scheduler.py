class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        cnt = Counter(tasks)
        maxFreq = max(cnt.values())                      # 最常見任務的次數
        numMax = sum(1 for v in cnt.values() if v == maxFreq)  # 有幾種任務都達到 maxFreq

        # 把最高頻任務當骨架：
        # 共有 (maxFreq - 1) 個「間隔」，每個間隔長度是 (n + 1)
        # 最後一格要放 numMax 個最高頻任務（因為可能有多個並列最高頻）
        skeleton = (maxFreq - 1) * (n + 1) + numMax

        # 若其他任務很多，能把 idle 填滿，最短時間至少是總任務數
        # skeleton 是冷卻造成的下限
        # len(tasks) 是工作量造成的下限
        return max(len(tasks), skeleton)



#maxFreq-1：A 之間有幾段要隔開
#n+1：每段長度（A + 冷卻 n 格）
#+numMax：最後一排尾巴有幾個並列第一的任務要放