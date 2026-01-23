class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        new_start, new_end = newInterval
        res = []
        insert = False

        for start, end in intervals:
            if end < new_start:
                res.append([start, end])
            elif new_end < start:
                if not insert:
                    res.append([new_start, new_end])
                    insert = True
                res.append([start, end])
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)

        if not insert:
            res.append([new_start, new_end])

        return res