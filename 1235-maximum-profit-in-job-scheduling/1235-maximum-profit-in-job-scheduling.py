class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        #積木一：整理資料 按照end time 排 (這步是為了讓二分搜有用)
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[1])
        n = len(jobs)

        #積木二：dp 存檔 
        #dp[i] 代表前 i 個工作能獲得的最大利潤
        #dp[0] = 0 作為 Base Case，處理找不到工作的情況
        dp = [0] * (n + 1)
        
        for i in range(len(jobs)):
            curr_start, curr_end, curr_profit = jobs[i]
            
            # 積木三：使用二分搜尋找「最後一個結束時間 <= 當前開始時間」的工作
            # 找的是第一個 > curr_start 的位置，所以 -1 就是最後一個 <=
            # 我們搜尋的範圍是之前的 jobs [0...i-1]
            l, r = 0, i
            best_prev_idx = 0 # 預設為 0，對應 dp[0]
            
            while l < r:
                mid = (l + r) // 2
                # 如果第 mid 個工作的結束時間 <= 當前開始時間
                if jobs[mid][1] <= curr_start:
                    # 這是一個潛在候選人，記錄下來並往右找更接近的
                    best_prev_idx = mid + 1 # +1 是因為要對齊 dp 的索引
                    l = mid + 1
                else:
                    r = mid
            
            # 選項 A: 不做這份工 (拿前一個 dp)
            # 選項 B: 做這份工 (當前獲利 + 歷史最大獲利)
            # 這裡 dp[idx] 就是那個不衝突的歷史獲利
            dp[i + 1] = max(dp[i], curr_profit + dp[best_prev_idx])
            
        return dp[len(jobs)]



#二分搜尋出場的時機：
#它幫你在那堆「已經排好結束時間的紀錄」裡，1 秒鐘找到那個「最晚且不衝突」的那筆
#當前最大獲利 = max( 不做這份工 , 做了這份工 + 之前能賺到的最大錢 )
    # 「不做」：就是存摺的前一筆資料 (dp[i])。
    # 「做了」：就是 當前錢 + 二分搜尋找回來的舊錢。


#二分搜尋：負責找「誰有資格跟我搭配」（時間不衝突）。
#DP 表：負責告訴你「跟那個人搭配，過去最高能拿多少錢」。
#這就是為什麼這題不需要 for 迴圈回去找最大值，因為最大值一直都跟著時間軸在更新。