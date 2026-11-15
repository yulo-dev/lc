class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        
        intervals.sort()

        prev_start = None
        prev_end = None

        for start, end in intervals:
            if prev_start == None and prev_end == None:
                prev_start = start
                prev_end = end

            else:
                if prev_end > start:
                    return False
                else:
                    prev_start = start
                    prev_end = end

        return True

