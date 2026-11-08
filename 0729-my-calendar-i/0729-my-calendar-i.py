class MyCalendar:

    def __init__(self):
        self.booking = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.booking:
            self.booking.append([startTime, endTime])
            return True
        else:
            for old_start, old_end in self.booking:
                if old_start < endTime and startTime < old_end:
                    return False
               
        self.booking.append([startTime, endTime])
        return True
        
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)