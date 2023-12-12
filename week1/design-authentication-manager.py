class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeTolive = timeToLive
        self.tokenIds = {}
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenIds[tokenId] = currentTime
    def renew(self, tokenId: str, currentTime: int) -> None:
        if ( tokenId in self.tokenIds and currentTime < self.tokenIds[tokenId] + self.timeTolive):
            self.tokenIds[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for val in self.tokenIds:
            if ( self.tokenIds[val] + self.timeTolive > currentTime):
                count += 1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)