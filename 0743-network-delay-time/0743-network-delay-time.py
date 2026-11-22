class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        #build graph
        graph = defaultdict(list)
        
        for time in times:
            node = time[0]
            neighbor = time[1]
            weight = time[2]

            graph[node].append((neighbor, weight))

        #Dijkstra
        best_dict = {k:0}
        heap = [(0,k)]

        while heap:
            curr_dist, node = heapq.heappop(heap)

            #best_dist 已經更新，但 Heap 裡可能還留著舊資料。
            #Lazy Deletion（延遲刪除）
            if curr_dist > best_dict[node]:
                continue

            for neighbor, weight in graph[node]:
                new_dist = curr_dist + weight
                
                if new_dist < best_dict.get(neighbor, float("inf")):
                    best_dict[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        return max(best_dict.values()) if len(best_dict) == n else -1