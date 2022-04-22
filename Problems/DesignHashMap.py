class MyHashMap:

    def __init__(self):
        self.size = int(1e6)
        self.data = [None] * self.size

    def put(self, key: int, value: int) -> None:
        v = key % self.size
        self.data[v] = (key,value)

    def get(self, key: int) -> int:
        v = key % self.size
        if self.data[v]:
            return self.data[v][1]
        else:
            return -1

    def remove(self, key: int) -> None:
        v = key % self.size
        self.data[v] = None
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
