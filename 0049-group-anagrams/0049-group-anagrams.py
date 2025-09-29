from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        
        freq = defaultdict(list)

        for ch in strs:
            key = ''.join(sorted(ch))
            freq[key].append(ch)
        
        return list(freq.values())
        