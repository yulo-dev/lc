class Solution:
    def reverseWords(self, s: str) -> str:
        #key word: reverse word, seperate by space, remove extra space: split or two pointers

        s_split = s.split()
        res = []

        for i in range(len(s_split)-1, -1, -1):
            res.append(s_split[i])

        return " ".join(res)
    