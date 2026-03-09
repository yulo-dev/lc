class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict) #time complexity from O(k) to O(1)
        n = len(s)
        #dp[i] represents whether the prefix of string s of length i can be segmented into words from the dictionary.
        #First, I define a DP array called dp with a length of n + 1. The index i here corresponds to the prefix length.
        dp = [False] * (n + 1) 

        #dp[0] is my base case. It represents an empty string, which is always considered 'valid' or 'segmentable' by default.
        dp[0] = True
        
        for i in range(n):
            if not dp[i]: #這邊在控制每一段的起點 他的起點要是True 代表合法起點 才能湊 
                continue
            
            for j in range(i + 1, n + 1):
                if s[i:j] in wordset: # 這裡在檢查「目前的切塊」在不在字典裡, 如果在, 就把這個位置標記為「可到達」
                    dp[j] = True

        #I return dp[n] because it indicates whether there exists at least one sequence of words 
        #that can perfectly cover the entire string from the very beginning to the very last character, without leaving any gaps.
        return dp[n] #n 是字串的總長度。如果 dp[n] 是 True，代表有一個單字它的結尾剛好落在索引 n, 且前面也是通的, 這形成了一條從 dp[0] 一路通往 dp[n] 的完整路徑
        

#這題基本的解法就是hashset + dp
#如果考慮空間複雜度或是被問「如果 wordDict 非常大，或者字串切片開銷太大怎麼辦？」，這時候可用 Trie 解決
#因為hashset每個字會獨立存, trie如果有重複的prefix只會存一次, 有不同的才會額外存, 可以省空間