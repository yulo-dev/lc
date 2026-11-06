class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        mapping = defaultdict(list) #key=sorted word, value = corresponding original strings

        for s in strs:
            keys = str(sorted(s))
            mapping[keys].append(s)

        return list(mapping.values())