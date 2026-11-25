class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        
        #buld graph
        graph = defaultdict(list)
        for i in range(len(edges)):
            node1 = edges[i][0] 
            node2 = edges[i][1] 
            weight = succProb[i]

            graph[node1].append((node2, weight))
            graph[node2].append((node1, weight))

        #dict: collect max path from start node
        #heap : collect each path from start node

        best_dist = {start_node:1}
        import heapq
        heap = [(-1, start_node)]

        while heap:
            curr_dist, node = heapq.heappop(heap)
            curr_dist = curr_dist * -1

            if curr_dist < best_dist[node]:
                continue

            for nei, weight in graph[node]:
                new_weight = curr_dist * weight

                if new_weight > best_dist.get(nei, float("-inf")):
                    best_dist[nei] = new_weight
                    heapq.heappush(heap, (-new_weight, nei))

        if end_node not in best_dist:
            return 0
        else:
            return best_dist[end_node] 
                



