class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        sz = len(strs[0])
        for s in strs:
            sz = min(sz, len(s))

        res = ""

        for i in range(sz):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[j-1][i]:
                    return res

            res += strs[0][i]

        return res
