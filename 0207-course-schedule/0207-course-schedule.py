class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        num_complete = 0

        while queue:
            course = queue.popleft()
            num_complete += 1
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return num_complete == numCourses

 