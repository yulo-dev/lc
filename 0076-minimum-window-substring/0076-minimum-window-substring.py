class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_cnt = Counter(t)
        window = Counter()

        formed = 0  #count how many alphbets met the freq as t_cnt

        left = 0
        best_len = float("inf")
        best_left = 0

        for right, val in enumerate(s):
            window[val] += 1

            if val in t_cnt and window[val] == t_cnt[val]:
                formed += 1
            
            while formed == len(t_cnt):     #當此window已經滿足t, 就開始嘗試縮小window

                if (right - left + 1) < best_len: #這邊是在記錄答案,最後要回傳
                    best_len = right - left + 1
                    best_left = left

                window[s[left]] -= 1 #這邊是在縮減

                if s[left] in t_cnt and window[s[left]] < t_cnt[s[left]]: #如果縮減到的剛好是在t裡面的字母 就要檢查頻率動到的程度是不是已經不滿足t
                    formed -= 1
                
                left += 1 #這邊是在縮減

        if best_len == float("inf"):
            return ""
        else:
            return s[best_left:best_left + best_len]
        