class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        #zip() 最重要的限制就是：只會配到最短的那個長度，超出的元素會被「默默忽略」。
        #所以才要先做長度的比對 不然可能少比到後面的字母或單字 但沒發現
        if not pattern or not s:
            return False

        words = s.split()

        if len(pattern) != len(words):
            return False


        #作法二
        #以 pattern="abba", words=["dog","cat","cat","dog"] 為例：
        #a 必須永遠對應到 dog, b 必須永遠對應到 cat
        #不能出現：同一個字母對到不同單字，或同一個單字被兩個字母共用
        # 只用一張 p2w 只能防止「同字母對不同單字」，但防不了「不同字母對同單字」；第二張 w2p 補上這個限制

        p2w = {} # pattern char -> word
        w2p = {} # word -> pattern char

        for ch, w in zip(pattern, words):
            if ch in p2w and p2w[ch] != w: 
                return False 
                
            if w in w2p and w2p[w] != ch: 
                return False 
                
            p2w[ch] = w 
            w2p[w] = ch

        return True