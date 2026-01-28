class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]
        in_degree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u) 
            in_degree[u] += 1
            in_degree[v] += 1

        queue = deque()
        for i in range(n):
            if in_degree[i] == 1:
                queue.append(i)

        remaining = n
        while remaining > 2:
            size = len(queue)
            remaining -= size

            for i in range(size):
                leaf = queue.popleft()
                for new_leaf in graph[leaf]:
                    in_degree[new_leaf] -= 1
                    if in_degree[new_leaf] == 1:
                        queue.append(new_leaf)

        return list(queue)