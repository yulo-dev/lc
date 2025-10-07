class Solution:
    def arrangeWords(self, text: str) -> str:
        lower_text = text.lower()
        split_text = lower_text.split()
        sort_text = sorted(split_text, key = len)
        res = ' '.join(sort_text)
        return res.capitalize()