class UndergroundSystem:

    def __init__(self):
        self.checkInInformation = {}
        self.timeTotal = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInInformation[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkInInformation[id]
        if (startStation, stationName) in self.timeTotal:
            self.timeTotal[(startStation, stationName)].append(t - startTime)
        else:
            self.timeTotal[(startStation, stationName)] = [t - startTime]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return float(sum(self.timeTotal[(startStation, endStation)])) / len(self.timeTotal[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
