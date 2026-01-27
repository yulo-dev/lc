class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses
        
        #建圖
        # build graph + indegree
        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            in_degree[node_in] += 1
        
        queue = deque()
        
        # 將indegree=0的編號加入queue
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        #queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        num_choose = 0
        while queue:
            now_pos = queue.popleft()
            num_choose += 1
            # 將鄰邊刪掉，如果indegree=0，再加入queue
            for next_pos in graph[now_pos]:
                in_degree[next_pos] -= 1
                if in_degree[next_pos] == 0:
                    queue.append(next_pos)
        
        return num_choose == numCourses