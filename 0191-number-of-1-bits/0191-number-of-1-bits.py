class Solution:
    def hammingWeight(self, n: int) -> int:

        res = 0

        #直接呼叫 不用轉list 也可以itertae
        #如果想跳過"ob"這個開頭 就寫 bin(n)[2:]
        
        for l in bin(n):
            if l == '1':
                res += 1

        return res