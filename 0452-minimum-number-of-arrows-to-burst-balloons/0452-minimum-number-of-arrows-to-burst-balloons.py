class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key = lambda x: x[1])

        res = 1
        prev_end = points[0][1]

        for i in range(1, len(points)):
            if prev_end < points[i][0]:
                res += 1
                prev_end = points[i][1]
        
        return res
