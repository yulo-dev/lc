class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        sentence_sort = ''.join(sorted(set(sentence)))
        return alpha == sentence_sort