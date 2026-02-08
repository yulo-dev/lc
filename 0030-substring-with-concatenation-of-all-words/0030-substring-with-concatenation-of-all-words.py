class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        L = len(words[0]) #單字長度
        k = len(words) #總共幾個單字
        total = L * k
        n = len(s)

        need = Counter(words)
        res = []

        for offset in range(L):
            left = offset
            seen = defaultdict(int) #這個 window 裡每個 word 出現幾次
            count = 0  # how many words currently in window (validly tracked)

            for right in range(offset, n - L + 1, L):
                w = s[right:right+L]

                # 這個 token 根本不在 words 裡，所以任何包含它的 window 都不可能是答案。
                # 因此我直接「重置」window，從 right+L 重新開始。
                # 1) 確保window 裡的每個 token 一定是合法單字
                if w not in need:
                    seen.clear()
                    count = 0
                    left = right + L
                    continue

                seen[w] += 1
                count += 1

                # shrink if too many of w
                # 確保 2) window 裡每個單字的次數都不會超過 need
                while seen[w] > need[w]:
                    left_w = s[left:left+L] #找左邊那個 token
                    seen[left_w] -= 1 #把它從 window 移除
                    count -= 1
                    left += L


                # if window has k words, record
                # 因為前面做了所有嚴格檢查，最後只剩「長度是否剛好」這個門檻
                # 因為在進到 if count == k 之前，我們已經確保兩件事：
                    #1) window 裡的每個 token 一定是合法單字
                    #2) window 裡每個單字的次數都不會超過 need
                if count == k:
                    res.append(left)
                    # move left by one word to continue searching
                    left_w = s[left:left+L]
                    seen[left_w] -= 1
                    count -= 1
                    left += L

        return res