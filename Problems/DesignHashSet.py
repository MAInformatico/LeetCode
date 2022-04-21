class MyHashSet:

    def __init__(self):
        self.data = set()
        

    def add(self, key: int) -> None:
        self.data.add(key)
        return None

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)
        return None

    def contains(self, key: int) -> bool:
        if key in self.data:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
