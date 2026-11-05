class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        graph = []
        for _ in range(numCourses):
            graph.append([])

        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        from collections import deque
        queue = deque()
        for course in range(len(in_degree)):
            if in_degree[course] == 0:
                queue.append(course)

        cnt = 0
        while queue:
            course = queue.popleft()
            cnt += 1
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return cnt == numCourses