class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n_char = str(n)

        non_zero = ""
        sum = 0

        for ch in n_char:
            if ch != "0":
                non_zero += ch
                sum += int(ch)

        if not non_zero:
            return 0
             
        return int(non_zero) * sum