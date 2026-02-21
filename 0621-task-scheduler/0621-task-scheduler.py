class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        cnt = Counter(tasks)
        h = [-freq for freq in cnt.values()]
        heapq.heapify(h)

        queue = deque()
        time = 0 

        while h or queue:
            time += 1
            if h:
                freq = heapq.heappop(h) + 1

                if freq != 0:
                    queue.append((freq, time+n))
            
            while queue and queue[0][1] <= time:
                heapq.heappush(h, queue.popleft()[0])

        return time