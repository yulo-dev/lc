class Solution:
    def arrangeWords(self, text: str) -> str:
        lower_text = text.lower()
        word_spilt = lower_text.split(" ")
        word_sort = sorted(word_spilt, key = len)
        res = ' '.join(word_sort)
        return res.capitalize()