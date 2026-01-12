class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""

        res = ""

        for i in range(len(strs[0])): #把 strs[0] 當作基準，因為共同前綴不可能比它更長
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            
            res += strs[0][i]

        return res