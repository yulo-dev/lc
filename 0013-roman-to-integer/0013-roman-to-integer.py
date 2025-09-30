class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        tot = 0
        prev = 0

        for ch in s:
            val = mapping[ch]
            if prev < val:
                tot += val - 2 * prev
            else:
                tot += val
            prev = val
        return tot