class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)] #代表類似 graph[0]：從課程 0 出發可以到哪些課
        in_degree = [0] * numCourses # in_degree[i] = 有多少門先修課指向 i（i 還缺幾個 prerequisite）
        
        #建圖
        # build graph + indegree
        #[course, prereq] means prereq -> course
        for course, prereq in prerequisites:
            graph[prereq].append(course) 
            in_degree[course] += 1
        
        queue = deque()
        
        # 將indegree=0的編號加入queue
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        #queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        num_choose = 0
        while queue: #只要還有可以修的課，就繼續修
            course = queue.popleft() #拿出一門「現在可修」的課，準備把它修掉
            num_choose += 1 #計數：我已經成功修完一門課

            # 看「修完 course 之後，哪些課會被解鎖/受影響」，如果indegree=0，再加入queue
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        return num_choose == numCourses