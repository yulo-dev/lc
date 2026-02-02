class Solution:
    def reverseWords(self, s: str) -> str:
        #key word: reverse word, seperate by space, remove extra space: split or two pointers
        word = s.split()
        res = []
        for i in range(len(word)-1, -1, -1):
            res.append(word[i])

        return " ".join(res)
