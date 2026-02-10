class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        if not pattern or not s:
            return False

        words = s.split()

        if len(pattern) != len(words):
            return False

        def encode(items):
            mapping = {}
            res = []
            for ch in items:
                if ch not in mapping:
                    mapping[ch] = len(mapping)
                res.append(mapping[ch])
            return res

        return encode(pattern) == encode(words)