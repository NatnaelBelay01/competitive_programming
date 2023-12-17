class FrequencyTracker:

    def __init__(self):
        self.track = {}
        self.freq = {}
    def add(self, number: int) -> None:
        freq = self.track.get(number, 0)
        self.freq[freq] = self.freq.get(freq , 0) - 1
        if (self.freq[freq] < 1):
            self.freq.pop(freq)
        self.track[number] = self.track.get(number, 0) + 1
        new_freq = self.track[number]
        self.freq[new_freq] = self.freq.get(new_freq , 0) + 1
    def deleteOne(self, number: int) -> None:
        freq = self.track.get(number , 0)
        self.freq[freq] = self.freq.get(freq, 0) - 1
        if (self.freq[freq] < 1):
            self.freq.pop(freq)
        self.track[number] = self.track.get(number, 0) - 1
        if (self.track[number] < 1):
            self.track.pop(number)
        else:
            new_freq = self.track[number]
            self.freq[new_freq] = self.freq.get(new_freq, 0) + 1
    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq

        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)