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
        
        def dfs(index, node):
            cur = node
            
            for i in range(index, len(word)):
                ch = word[i]

                #. 分支是窮舉匹配（Exhaustive Search），我們對當前節點的所有子節點發起遞迴
                if ch == ".":
                    #嘗試目前房間裡「所有的門」。
                    for child_node in cur.children.values():
                        if dfs(i+1, child_node): # 派一個分身，帶上「剩下的字串」，進去這扇門
                            return True # 只要有一個分身成功了，我就大喊成功
                    return False

                #else 分支是強匹配（Exact Match），我們直接沿著字典樹往下走
                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch]
            return cur.is_end
    
        return dfs(0, self.root)
        
#關鍵在於cur = cur.children[ch] 如果遇到ch="."會報錯
#因為Trie裡面存的是"a","b","c"... 沒有一個key叫"."
#當遇到"."，我們不能只進一扇門，我們要變成「分身」, 只要其中一個分身回報「我找到終點了！」，整個 search 就回傳 True
#遇見字母：直接走進對應的房間。
#遇見點號：像是遇到了分岔路，你必須用 for 迴圈把當前房間裡所有能走的路都試一遍。
#遞迴 (DFS)：幫助你處理「試了一半發現不行，要退回分岔路再試另一條」的情況。
#看到 「多選一」 或 「多種可能性」 的搜尋，通常就是 DFS 派上用場的時候。

         


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)