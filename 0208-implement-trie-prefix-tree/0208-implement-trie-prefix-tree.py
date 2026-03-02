class TreeNode:
    def __init__(self):
        #For each Trie node, I store a dictionary called children to map a character to the next node, 
        #and a boolean is_end to mark whether this node is the end of a complete word.
        self.children = {} #Key 是字母，Value 是下一個 Trie 節點, children 為什麼是 dict: 因為一個 node 下面可能接很多不同字母，
        self.is_end = False #用來標記「到這格為止，是否構成一個完整的單字」

class Trie:
    def __init__(self):
       #In the Trie class, I initialize a root node. The root does not represent a character itself. It is just the starting point for all words.  
       self.root = TreeNode()


    #For insertion, I start from the root node and process the word one character at a time.
    #For each character, I check whether the current node already has that child. If not, I create a new node for that character.
    #Then I move curr to that child node and continue.
    #After processing all characters, I mark the last node as is_end = True to indicate that a complete word ends here.
    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            # 如果字母不在孩子裡，就開一個新的節點
            if ch not in cur.children:
                cur.children[ch] = TreeNode()

            # The line curr = curr.children[ch] means I move my pointer down to the next node for that character.
            # So I am basically walking down the Trie one level at a time.
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
        #If I successfully finish traversing the word, I still need to check curr.is_end.
        #That is because a path existing in the Trie does not necessarily mean the full word exists. It may only be a prefix.
        return cur.is_end
      

    #startsWith is similar to search, but here I only care whether the prefix path exists.
    #So if I can traverse all characters in the prefix successfully, I return True.
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