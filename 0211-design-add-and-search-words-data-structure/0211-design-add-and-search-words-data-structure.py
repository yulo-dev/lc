class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        
        cur.is_end = True

    def search(self, word: str) -> bool:

        def dfs(cur, i):
            if i == len(word):
                return cur.is_end

            ch = word[i]
            if ch == ".":
                for nxt in cur.children.values():
                    if dfs(nxt, i + 1):
                        return True
                return False
            else:
                if ch not in cur.children:
                    return False
                return dfs(cur.children[ch], i + 1)

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)