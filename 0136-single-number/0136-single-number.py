class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        #任何數字跟 0 做 XOR，都不會改變原本的數字
        res = 0

        #因為 XOR 有兩個重要規則：
            #0 ^ a = a：0 跟任何數字做 XOR，結果是原本的數字。
            #a ^ a = 0：相同的數字做 XOR，結果是 0。
            #所以你可以想成：兩個相同的數字會互相抵消。

        for num in nums:
            res = res ^ num

        return res


        #二進位制
        #0000 -> 1
        #0001 -> 2
        #0010 -> 3
        #0011
        #0100
        #0101
        #0110
        #0111
        #1000
        #1001 -> 10
        #1010
        #1011
        #1100
        #1110
        #1111 -> 15
        #10000 -> 16