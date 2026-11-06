class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()
        if len(pattern) != len(words):
            return False

        mapping = {}

        visited = set()

        for ch, word in zip(pattern, words):
            if ch in mapping:
                if mapping[ch] != word:
                    return False
            else:
                if word in visited:
                    return False
                mapping[ch] = word
                visited.add(word)

        return True
            
