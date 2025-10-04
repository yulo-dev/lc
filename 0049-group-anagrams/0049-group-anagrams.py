from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        mapping = defaultdict(list)

        for s in strs:
            keys = ''.join(sorted(s))
            mapping[keys].append(s)
        
        return list(mapping.values())