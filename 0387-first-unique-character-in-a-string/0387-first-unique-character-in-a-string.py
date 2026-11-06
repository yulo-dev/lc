class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freq = defaultdict(int) #ch: count
        idx = defaultdict(int)


        for i, ch in enumerate(s): 
            freq[ch] += 1
            if ch not in idx:
                idx[ch] = i

        for ch, cnt in freq.items():
            if cnt == 1:
                return idx[ch]

        return -1


        