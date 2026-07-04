class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        #build graph
        graph = defaultdict(list)
        visited = set()
        for start, end, weight in roads:
            graph[start].append([end, weight])
            graph[end].append([start, weight])

        queue = deque([1])
        visited.add(1)
        res = float('inf')

        res = self.bfs(queue, graph, visited, res)

        return res

    def bfs(self, queue, graph, visited, res):

        while queue:
            node = queue.popleft()
            for end, weight in graph[node]:
                res = min(res, weight)
                if end not in visited:
                    queue.append(end)
                    visited.add(end)

        return res