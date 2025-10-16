from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = defaultdict(list)

        for st in strs:
            keys = ''.join(sorted(st))
            anagram_dict[keys].append(st)

        return list(anagram_dict.values())