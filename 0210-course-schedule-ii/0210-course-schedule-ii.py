class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            for new_course in graph[course]:
                in_degree[new_course] -= 1
                if in_degree[new_course] == 0:
                    queue.append(new_course)

        return res if len(res) == numCourses else []


