class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        i , j = 0, len(skill) - 1
        chek = skill[i] + skill[j]
        while (i < j):
            if (chek != skill[i] + skill[j]):
                return (-1)
            i += 1
            j -= 1
        i, j, chek = 0, len(skill) - 1, 0
        while (i < j):
            chek = chek + (skill[i] * skill[j])
            i += 1
            j -= 1
        return (chek)
        