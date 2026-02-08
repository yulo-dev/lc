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

        # 最困惑的是第一個跟第二個for loop 
        # 第一個for loop 只會從 0 ~ 單字長度 當作這個window的起始點, 這個window指的是words裡面單字一次排列的組合 不是指單一個單字
        # 第二個for loop 才會透過每 Ｌ 個跳一次, 去切割他總共跑完整串s, 就是逐個取出長度 L 的 token，掃完整個 Ｓ
        # left 代表「目前 sliding window 的起始 index」（永遠對齊 offset）
        # right是單一個token的起點
        for offset in range(L):
            left = offset
            seen = defaultdict(int) 
            count = 0  

            for right in range(offset, n - L + 1, L):
                w = s[right:right+L]

                if w not in need:
                    seen.clear() #清空 即便剛剛前面有找到幾個吻合的單字 但不能用 因為已經混雜其他不對的單字了 直接清空重新搜集
                    count = 0 
                    left = right + L
                    continue

                seen[w] += 1
                count += 1

                while seen[w] > need[w]:
                    need_remove = s[left:left+L] 
                    seen[need_remove] -= 1
                    count -= 1
                    left += L

                if count == k:
                    res.append(left)
                    need_remove = s[left:left+L]
                    seen[need_remove] -= 1
                    count -= 1
                    left += L

        return res