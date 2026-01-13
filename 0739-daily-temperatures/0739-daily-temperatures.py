class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                cooler_date = stack.pop()
                res[cooler_date] = i - cooler_date

            stack.append(i)

        return res