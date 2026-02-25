class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends) # 優化查詢速度至 O(1)

        if "0000" in dead_set: # 邊界情況：起點就是死路
            return -1

        queue = deque(["0000"])
        visited = {"0000"}
        turns = 0 # 撥動次數從 0 開始

        while queue:
            for _ in range(len(queue)):
                num = queue.popleft()
                if num == target:
                    return turns

                for new_num in self.generate_num(num):
                    if new_num in visited or new_num in dead_set:
                        continue
                    queue.append(new_num)
                    visited.add(new_num)
            turns += 1

        return -1 # 走不到終點

    def generate_num(self, num):
        res = []
        for i in range(4): # 4 個轉盤
            digit = int(num[i])
            # 向上 (+1) 或 向下 (-1)
            for move in [1, -1]:
                new_digit = (digit + move) % 10 # 處理 0 與 9 的循環
                res.append(num[:i] + str(new_digit) + num[i+1:])
        return res 

