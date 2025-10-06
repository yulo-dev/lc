class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        queue = deque([("", 0, 0)])

        while queue:
            substring, open_cnt, close_cnt = queue.popleft()
            if len(substring) == (n*2):
                res.append(substring)
                continue
            if open_cnt < n:
                queue.append((substring + "(", open_cnt+1, close_cnt))
            if close_cnt < open_cnt:
                queue.append((substring + ")", open_cnt, close_cnt+1))
        return res