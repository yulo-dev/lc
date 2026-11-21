class Solution:
    def hammingWeight(self, n: int) -> int:

        res = 0

        res += bin(n).count('1')

        return res