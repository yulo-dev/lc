class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []

        for i in range(1, n+1):
            temp = []
            #因為用了兩個獨立的 if，所以 15 會同時加入 "Fizz" 和 "Buzz"，再用 "".join(temp) 合成 "FizzBuzz"
            if i % 3 == 0:
                temp.append("Fizz")
            if i % 5 == 0:
                temp.append("Buzz")
            if not temp:
                res.append(str(i))
            else:
                res.append("".join(temp))

        return res