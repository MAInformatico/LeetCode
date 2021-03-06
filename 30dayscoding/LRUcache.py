from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.dictLRU = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dictLRU:
            return -1
        else:
            self.dictLRU.move_to_end(key)
            return self.dictLRU[key]
        
    def put(self, key: int, value: int) -> None:
        if key not in self.dictLRU:
            if len(self.dictLRU) >= self.cap:
                self.dictLRU.popitem(last=False) 
        else:
            self.dictLRU.move_to_end(key) 
            
        self.dictLRU[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
