class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        from collections import deque
        queue = deque()

        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
                
        res = []

        while queue:
            course = queue.popleft()
            res.append(course)

            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
                    #所有課程都成功排進修課順序
        return res if len(res) == numCourses else []