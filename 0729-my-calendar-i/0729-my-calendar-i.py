class MyCalendar:

    def __init__(self):
        self.booking = []

    def book(self, startTime: int, endTime: int) -> bool:
        for old_start, old_end in self.booking:
            if old_start < endTime and startTime < old_end:
                return False
               
        self.booking.append([startTime, endTime])
        return True

        #not overlap: old end <= new start or new end <= old start 
        #overlap: old end > new start and new end > old start 
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)