class Solution:
    def hammingWeight(self, n: int) -> int:
        lis = list(bin(n))

        res = 0

        for l in lis:
            if l == '1':
                res += 1

        return res