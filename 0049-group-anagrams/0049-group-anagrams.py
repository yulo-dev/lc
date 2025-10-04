from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        mapping = defaultdict(list)

        for ch in strs:
            keys = ''.join(sorted(ch))
            mapping[keys].append(ch)

        return list(mapping.values())