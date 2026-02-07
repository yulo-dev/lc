class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        h = []
        res = []

        for right, x in enumerate(nums):
            heapq.heappush(h, (-x, right))

            #窗口大小 k 已經湊滿了，所以你現在才有資格開始輸出答案（window max）
            #其實也就是 每個 right ≥ k-1 都要輸出一次
            if right >= k -1:
                left = right - k + 1 #代表 目前滑動窗口（window）的左邊界 index

                # 這邊因為 heap 做的是 lazy deletion：
                # 過期的元素可以先留著沒關係，只要它沒跑到堆頂（h[0]）就不影響答案。
                # 等哪天它真的跑到堆頂，才會被 while h[0][1] < left pop 掉。

                # 如果 候選的 index < left → 代表它在「目前 window 的左邊外面」 → 完全不在這個 window 內（過期）
                # → 必須 pop 掉，不能拿它當最大值
                # 這就是 lazy deletion：只有當過期元素跑到堆頂、會影響答案時，才移除
                while h[0][1] < left:
                    heapq.heappop(h)

                #經過 while h[0][1] < left 之後，h[0] 會變成 「一定還在窗口內的最大值候選」
                #append 的就是 當前 window 的最大值
                res.append(-h[0][0])

        return res