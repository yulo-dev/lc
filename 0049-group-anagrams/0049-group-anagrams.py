from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for ch in strs:
            keys = ''.join(sorted(ch))
            anagram_dict[keys].append(ch)

        return list(anagram_dict.values())