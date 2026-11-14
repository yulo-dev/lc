class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]

        curr.is_end = True

    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        for s in strs:
            self.insert(s)

        curr = self.root
        res = ""

        while len(curr.children) == 1 and not curr.is_end:
            for key, child in curr.children.items():
                res += key
                curr = child

        return res