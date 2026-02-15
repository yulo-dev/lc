class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # initialize result 
        res = []

        # 1 indexed
        for i in range(1, n+1):
            temp = []
            if i % 3 == 0:
                temp.append("Fizz") 
            if i % 5 == 0:
                temp.append("Buzz")  
            if not temp:
                res.append(str(i))
            else:
                res.append("".join(temp))

        return res 
                