class UndergroundSystem:

    def __init__(self):
        self.destinations = {}
        self.time_taken = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.destinations[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        initial = self.destinations[id][0]
        time = self.destinations[id][1]
        journey = initial + '->' + stationName
        if (journey not in self.time_taken):
            self.time_taken[journey] = []
        self.time_taken[journey].append(t - time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        journey = startStation + '->' + endStation
        total = sum(self.time_taken[journey])
        length = len(self.time_taken[journey])
        return total / length


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)