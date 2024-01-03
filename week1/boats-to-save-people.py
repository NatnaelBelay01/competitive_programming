class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        count = 0
        last = len(people) - 1
        first = 0

        while (first <= last):
            if(people[last] + people[first] > limit):
                count += 1
                last -= 1
            else:
                count += 1
                last -= 1
                first += 1
  
        return count
            