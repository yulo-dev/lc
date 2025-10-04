class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.bfs(n)

    def bfs(self, n):
        res = []
        queue = deque()
        # 每個元素存 (當前字串, open數量, close數量)
        queue.append(("", 0, 0))

        while queue:
            cur, open_cnt, close_cnt = queue.popleft()

            # 如果長度 == 2*n，代表完成一個有效字串
            if len(cur) == 2 * n:
                res.append(cur)
                continue

            # 可以加 "("
            if open_cnt < n:
                queue.append((cur + "(", open_cnt + 1, close_cnt))

            # 可以加 ")"
            if close_cnt < open_cnt:
                queue.append((cur + ")", open_cnt, close_cnt + 1))

        return res