class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I":"1", "V":"5", "X":"10", "L":"50", "C":"100", "D":"500", "M":"1000"}
        stack = []
        tot = 0

        for i, ch in enumerate(s):
            if i > 0:
                prev = stack.pop()
                if prev == "I" and (ch == "V" or ch == "X"):
                    tot -= 2
                elif prev == "X" and (ch == "L" or ch == "C"):
                    tot -= 20
                elif prev == "C" and (ch == "D" or ch == "M"):
                    tot -= 200

            tot += int(mapping[ch])
            stack.append(ch)

        return tot