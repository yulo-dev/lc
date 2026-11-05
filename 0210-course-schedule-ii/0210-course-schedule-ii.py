class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = []
        for _ in range(numCourses):
            graph.append([])

        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        from collections import deque
        queue = deque()
        res = []
        for course in range(len(in_degree)):
            if in_degree[course] == 0:
                queue.append(course)
                res.append(course)

        cnt = 0
        while queue:
            course = queue.popleft()
            cnt += 1
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
                    res.append(next_course)

        return res if cnt == numCourses else []

        


