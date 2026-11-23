class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        
        from collections import defaultdict
        graph = defaultdict(list)

        for i in range(len(edges)):
            start = edges[i][0]
            nei = edges[i][1]
            weight = succProb[i]
            graph[start].append((nei, weight))
            graph[nei].append((start, weight))

        max_path = {}
        max_path[start_node] = 1

        import heapq
        heap = [(-1, start_node)]

        while heap:
            curr_dist, node = heapq.heappop(heap)
            curr_dist = -1 * curr_dist

            if curr_dist < max_path[node]:
                continue

            for nei, dist in graph[node]:
                new_weight = dist * curr_dist
                if new_weight > max_path.get(nei, float("-inf")):
                    max_path[nei] = new_weight
                    heapq.heappush(heap, (-new_weight, nei))
        
        return max_path[end_node] if end_node in max_path else 0