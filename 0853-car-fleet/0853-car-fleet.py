class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # position big -> small
        stack = []  # store fleet arrival times

        for p, s in cars:
            t = (target - p) / s
            # if current car catches up to the fleet ahead, merge (do not push new fleet)
            if stack and t <= stack[-1]:
                continue
            stack.append(t)

        return len(stack)