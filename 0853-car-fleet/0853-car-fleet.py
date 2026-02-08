class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # 要排序的原因：
        # 只要你往終點方向看，後車只會追前車；而車隊形成後就等同一台車（不能超車）
        # 先看離終點最近的車：它前面沒車，一定自己成一隊（暫時）
        # 再往後看下一台：它只需要問「我追得到前面那個隊嗎？」: 追得到 → 合併; 追不到 → 新車隊

        cars = sorted(zip(position, speed), reverse = True)
        stack = []

        for p, s in cars:
            t = (target - p) / s

            if stack and stack[-1] >= t:
                continue
            
            stack.append(t)

        return len(stack)