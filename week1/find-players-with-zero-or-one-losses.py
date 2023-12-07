class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        match_results = {}
        ans = [[],[]]
        for game in matches:
            match_results[game[0]] = 0 + match_results.get(game[0], 0)
            match_results[game[1]] = 1 + match_results.get(game[1], 0)
        for player in match_results:
            if match_results[player] == 0:
                ans[0].append(player)
            if match_results[player] == 1:
                ans[1].append(player)
        ans[0].sort()
        ans[1].sort()
        return ans