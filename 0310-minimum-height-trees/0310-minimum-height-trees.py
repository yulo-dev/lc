class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)] #time: O(n); space: O(n+m)
        in_degree = [0] * n #time: O(n); space: O(n)

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
                for nei in graph[leaf]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 1:
                        queue.append(nei)

        return list(queue) 

#For a tree, we process each node once and each edge a constant number of times, so time is O(n). 
#We store the graph, degrees, and a queue, so space is O(n).
#因為這題是 樹, 樹的邊通常在算node的時候就cover進去了, 所以不用分開寫成 n + m
#但像是lc133 clone graph 因為他是一般圖 不是樹 所以要算 node + edge