class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mapping = {}
        
        for s in strs:
            keys = ''.join(sorted(s))
            if keys not in mapping:
                mapping[keys] = []
            mapping[keys].append(s)

        return list(mapping.values())
