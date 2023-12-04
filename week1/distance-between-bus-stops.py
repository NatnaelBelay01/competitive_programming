class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if (start == destination):
            return 0
        res1, res2 = 0, 0
        l = len(distance)
        i = start
        while (i != destination):
            res1 += distance[i]
            i = (i+1) % l
        i = destination
        while (i != start):
            res2 += distance[i]
            i = (i+1)%l
        return min(res1, res2)