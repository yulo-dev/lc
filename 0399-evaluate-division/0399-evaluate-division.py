class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # build the graph
        graph = defaultdict(list)

        for (a,b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1/val))
            
        #bfs
        res = []

        for start, end in queries:
            if start not in graph or end not in graph:
                res.append(-1.00000)
            elif start == end:
                res.append(1.00000)
            else:
                queue = deque([])
                visited = set()
                queue.append((start, 1.0))
                visited.add(start)
                self.bfs(start, end, graph, queue, visited, res)

        return res

    def bfs(self, start, end, graph, queue, visited, res):
        while queue:
            node, edge = queue.popleft()
            for nei, val in graph[node]:
                if nei not in visited:
                    queue.append((nei, edge * val))
                    visited.add(nei)
                    if nei == end:
                        res.append(edge * val)
                        return
                    
        res.append(-1.00000) 