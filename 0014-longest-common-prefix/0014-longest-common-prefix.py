class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                # 如果指標超出某個字串長度，或字元不匹配
                if i == len(s) or strs[0][i] != s[i]:
                    return res
        
            res += strs[0][i]

        return res