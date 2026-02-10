class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #用 set 才能 O(1) 查 x+1 在不在
        uni = set(nums)
        res = 0

        for n in uni:
            #只從「起點」開始數：n-1 不在 set 才表示 n 是新序列開頭
            if n - 1 not in uni:
                new_n = n
                # 從新序列開頭開始抓是不是有n+1 直到沒有n+1 代表不連續 才跳出while loop
                while new_n in uni:
                    new_n += 1
                res = max(res, new_n - n)

        return res