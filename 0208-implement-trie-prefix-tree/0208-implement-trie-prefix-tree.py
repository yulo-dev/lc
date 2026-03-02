class TreeNode:
    def __init__(self):
        self.children = {} #Key 是字母，Value 是下一個 Trie 節點, children 為什麼是 dict: 因為一個 node 下面可能接很多不同字母，
        self.is_end = False #用來標記「到這格為止，是否構成一個完整的單字」

class Trie:
    def __init__(self):
       self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            # 如果字母不在孩子裡，就開一個新的節點
            if ch not in cur.children:
                cur.children[ch] = TreeNode()
            cur = cur.children[ch]
        # 最後一個字母標記為結尾
        cur.is_end = True
       
    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        # 必須走到結尾標記才算找到完整單字
        return cur.is_end
      
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)