class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()        
        check = skill[0] + skill[-1]

        first = 0
        last = len(skill) - 1
        result = 0
        while(first < last):
            if(skill[first] + skill[last] != check):
                return -1
            result += skill[first] * skill[last]
            first += 1
            last -= 1
        
        return result