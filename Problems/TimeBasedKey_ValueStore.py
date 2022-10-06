class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key][timestamp] = value
        else:
            self.dict[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dict:
            for i in reversed(range(1, timestamp + 1)):
                if i in self.dict[key]:
                    return self.dict[key][i]
        
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
