class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """


        #每個字串我都用這個格式打包： "<長度>#<內容>", 且不是靠 # 來切內容，靠的是「長度」
        #例如 "ab" → 2#ab
        #"cat#dog" → 7#cat#dog（內容裡有 # 也沒差）

        out = []
        for s in strs:
            out.append(str(len(s)))
            out.append('#')
            out.append(s)
        return ''.join(out)


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        n = len(s)

        while i < n:
            #從 i 開始，找到下一個 #（用 j 走過去）
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            #用 length 切出內容
            start = j + 1 #為了跳過那個「長度結束用的 #」所以需要+1
            end = start + length
            res.append(s[start:end])

            #i 跳到下一段的開頭
            i = end
        return res

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))