class TrieNode:
    def __init__(self):
        self.children = {} 
        self.is_end = False
       
class Trie:
    def __init__(self):
        self.root = TrieNode() # 整棵 Trie 的起點

    def insert(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.is_end = True

    def search(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]

        return curr.is_end == True
   
    def startsWith(self, prefix):
        curr = self.root

        for p in prefix:
            if p not in curr.children:
                return False
            curr = curr.children[p]

        return True