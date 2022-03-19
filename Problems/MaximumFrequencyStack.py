class FreqStack:

    def __init__(self):
        self.data = []
        self.frequencies = defaultdict(int)

    def push(self, val: int) -> None:        
        self.frequencies[val] += 1
        if self.frequencies[val] > len(self.data):
            self.data.append([val])
        else:
            self.data[self.frequencies[val]-1].append(val)

    def pop(self) -> int:
        while not self.data[-1]:
            self.data.pop()
        val = self.data[-1].pop()
        self.frequencies[val] -= 1
        return val
    
    

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
