class MyQueue:
    
    def __init__(self):
        self.backup = []
        self.data = []

    def push(self, x: int) -> None:
        if len(self.data) == 0:
            self.data.append(x)
        else:
            while len(self.data)>0:
                self.backup.append(self.data.pop())
            self.data.append(x)
            while len(self.backup)>0:
                self.data.append(self.backup.pop())
            
    def pop(self) -> int:
        return self.data.pop()
        
    def peek(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:
        return len(self.data) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
