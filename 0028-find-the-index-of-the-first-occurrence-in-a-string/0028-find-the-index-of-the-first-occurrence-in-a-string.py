class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        hay_n = len(haystack)
        needle_n = len(needle)

        if needle_n > hay_n:
            return -1

        base = 256 #隨意取的 這邊是因為ASCII 一個 byte 0~255，用 256 當底數很常見
        mod = 10**9 + 7 #怕hash數字太大所以要取mod

        # base^(m-1) % mod，這邊是在計算最左邊那個字元的hash的權重，之後用來移除最左邊字元
        power = 1
        for _ in range(needle_n - 1):
            power = (power * base) % mod

        def code(ch):
            return ord(ch)  # 也可 ord(ch) - ord('a') + 1

        # needle hash
        target = 0
        for ch in needle:
            target = (target * base + code(ch)) % mod

        # first window hash
        window = 0
        for i in range(needle_n):
            window = (window * base + code(haystack[i])) % mod

        # check window i=0
        if window == target and haystack[0:needle_n] == needle:
            return 0

        # slide windows
        for i in range(1, hay_n - needle_n + 1):
            left_char = code(haystack[i - 1])
            right_char = code(haystack[i + needle_n - 1])

            # remove left char contribution
            window = (window - left_char * power) % mod
            # shift and add right char
            window = (window * base + right_char) % mod

            if window == target and haystack[i:i + needle_n] == needle:
                return i

        return -1