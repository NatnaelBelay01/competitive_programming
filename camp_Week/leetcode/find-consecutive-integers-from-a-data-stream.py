class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.queue.append(value)
        self.size = k
        self.count = 0

    def consec(self, num: int) -> bool:
        if len(self.queue) < self.size:
            if num != self.value:
                self.count += 1
            self.queue.append(num)
            return False
        else:
            temp = self.queue.popleft()
            if(num != self.value):
                self.count += 1
            self.queue.append(num)
            if temp != self.value:
                self.count -= 1
            if self.count == 0:
                return True
            return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)