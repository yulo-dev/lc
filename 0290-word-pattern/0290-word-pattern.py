class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping1 = defaultdict(list)
        mapping2 = defaultdict(list)

        res1 = []
        res2 = []

        for i, ch in enumerate(pattern):
            mapping1[ch].append(i)

        for val in mapping1.values():
            res1.append(val)
        
        for i, ch in enumerate(s.split()):
            mapping2[ch].append(i)

        for val in mapping2.values():
            res2.append(val)

        return res1 == res2