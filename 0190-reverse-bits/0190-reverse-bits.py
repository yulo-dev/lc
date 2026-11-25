class Solution:
    def reverseBits(self, n: int) -> int:
        
        
        binary = format(n, "032b") #把整數轉成 32-bit 的二進位字串
        new_binary = binary[::-1]  #反轉
        
        res = int(new_binary, 2) #二進位字串轉整數

        return res