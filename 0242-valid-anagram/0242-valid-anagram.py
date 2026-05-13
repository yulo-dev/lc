class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

#Python 的 dict（包含 Counter）在做 == 比較時，只看「是不是每個 key 都有，而且對應的 value 都一樣」，完全不管 key 的順序