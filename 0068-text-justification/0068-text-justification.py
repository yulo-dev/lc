class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        line_len = 0  # total letters (no spaces)

        #外面（分行那段）已經決定「這行有哪些字」，justify 只負責「怎麼塞空格」
        def justify(line_words: List[str], letters: int, is_last: bool) -> str:
            #step 1: 特殊規則（最後一行 or 只有一個字）
            # 最後一行也適用特殊規則在於 他的空格「主要塞在最後」，不像其他行要把空格分散塞在每個 gap 裡
            if is_last or len(line_words) == 1:
                s = " ".join(line_words)
                return s + " " * (maxWidth - len(s))

            #step 2: 一般行（不是最後一行，且至少兩個字）要 full justify
            gaps = len(line_words) - 1 #有幾個縫可以塞空格？
            total_spaces = maxWidth - letters #這行總共要塞多少空格？
            base = total_spaces // gaps #每個縫至少分到多少空格？
            extra = total_spaces % gaps  # 有多少個縫要多 1 格？如果 total_spaces 不能被 gaps 整除，會多出一些空格，題目要求「左邊優先多一格」

            #step 3: 真的把字串拼出來（按上面規則塞空格）
            out = []
            for i, w in enumerate(line_words):
                out.append(w)
                if i < gaps:
                    spaces = base + (1 if i < extra else 0)
                    out.append(" " * spaces)
            return "".join(out)

        for w in words:
            # if add w would exceed width
            if line_len + len(w) + len(line) > maxWidth:
                res.append(justify(line, line_len, is_last=False))
                line = []
                line_len = 0

            line.append(w)
            line_len += len(w)

        # last line
        res.append(justify(line, line_len, is_last=True))
        return res