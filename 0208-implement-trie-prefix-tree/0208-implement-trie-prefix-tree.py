class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for ch in word:
            #這邊是在說我到第幾個位子的這個字母有沒有出現過 不是單純這個字母有沒有出現過而已
            #如果已經做過app 那apple的時候的app就不用重複建TrieNode
            if ch not in cur.children:
                cur.children[ch] = TrieNode()

            #這邊就是把指標往下一個去移動
            #像是i += 1一樣的概念
            cur = cur.children[ch]

        #self.is_end：如果你寫在 Trie 類別裡面，那代表整棵樹只有一個開關
        cur.is_end = True

    def search(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]

        return cur.is_end

    def startsWith(self, prefix):
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]

        return True