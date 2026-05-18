class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        freq = defaultdict(int)
        res = 0
        for right in range(len(s)):
            freq[s[right]] += 1
            
            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res


# 擴張
#freq[s[right]] += 1       # 加進來

# 收縮
#freq[s[left]] -= 1        # 拿出去
#left += 1                 # 移動邊界


#while (right - left + 1) - max(freq.values()) > k:
    #We shrink the window when the window length minus the count of the most frequent character is greater than k. 
    #This means we need more than k replacements to make all characters the same, 
    #so the window is invalid and we need to shrink it.