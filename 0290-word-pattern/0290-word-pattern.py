class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        if not pattern or not s:
            return False

        words = s.split()

        if len(pattern) != len(words):
            return False

        mapping = defaultdict(int)
        cnt = 0
        pattern_1 = []

        for ch in pattern:
            if ch in mapping:
                pattern_1.append(mapping[ch])
            else:
                cnt += 1
                mapping[ch] = cnt 
                pattern_1.append(mapping[ch])


        mapping_2 = defaultdict(int)
        cnt_2 = 0
        pattern_2 = []

        for ch in words:
            if ch in mapping_2:
                pattern_2.append(mapping_2[ch])
            else:
                cnt_2 += 1
                mapping_2[ch] = cnt_2
                pattern_2.append(mapping_2[ch])

        return pattern_1 == pattern_2