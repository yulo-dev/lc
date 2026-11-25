class Solution:
    def calPoints(self, operations: list[str]) -> int:
        
        score = []

        for op in operations:
            if op == "+":
                tot = 0
                tot = score[-1]  + score[-2] 
                score.append(tot)
            elif op == "C":
                del score[-1] 
                #score.pop() 也可
            elif op == "D":
                num = score[-1] * 2
                score.append(num)
            else:
                score.append(int(op))

        res = 0
        for s in score:
            res += s

        return res
