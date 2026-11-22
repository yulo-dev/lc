class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for start, end, weight in times:
            graph[start].append((end, weight))

        best_weight = {k:0}
        heap = [(0,k)]

        while heap:
            curr_path, node = heapq.heappop(heap)

            if curr_path > best_weight[node]:
                continue

            for nei, weight in graph[node]:
                new_weight = curr_path + weight

                if new_weight < best_weight.get(nei, float("inf")):
                    best_weight[nei] = new_weight
                    heapq.heappush(heap,(new_weight, nei))
        
        return max(best_weight.values()) if len(best_weight) == n else -1