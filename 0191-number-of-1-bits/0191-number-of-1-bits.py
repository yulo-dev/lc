class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0

        while n > 0:
            res += n & 1  #use n bitwise AND one -> and Add the rightmost bit to the counter
            n >>= 1  #Shift n one bit to the right

        return res

        #I use bitwise AND with 1 to check the rightmost bit, then right-shift the number by one bit. 
        #I repeat this until the number becomes zero, counting all the set bits along the way.