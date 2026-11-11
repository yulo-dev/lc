class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mapping = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            mapping[key].append(word)

        return list(mapping.values())
