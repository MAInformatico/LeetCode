class MyCalendar:

    def __init__(self):
        self.days = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.days:
            if i < end and start < j:
                return False
        self.days.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
