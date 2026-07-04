class UndergroundSystem:

    def __init__(self):
        self.check_in = {}              
        self.route_stats = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in[id]
        self.route_stats[(start_station, stationName)].append(t - start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.route_stats[(startStation, endStation)]) / len(self.route_stats[(startStation, endStation)])
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)