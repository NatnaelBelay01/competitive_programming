class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cpty = capacity
        l = len(plants)
        step = 0
        for i in range(l):
            cpty -= plants[i]
            if(cpty < 0):
                cpty = capacity - plants[i]
                step += i * 2 + 1
            else:
                step += 1
        return step