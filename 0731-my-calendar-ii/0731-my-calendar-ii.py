class MyCalendarTwo:

    def __init__(self):
        self.booking = []
        self.double = []
        
    def book(self, startTime: int, endTime: int) -> bool:
        for double_start, double_end in self.double:
            if double_end > startTime and double_start < endTime:
                return False

        for old_start, old_end in self.booking:
            if old_end > startTime and old_start < endTime:
                dup_start = max(old_start, startTime)
                dup_end = min(old_end, endTime)
                self.double.append([dup_start, dup_end])
        
        self.booking.append([startTime, endTime])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)