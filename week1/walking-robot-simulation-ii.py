class Robot:

    def __init__(self, width: int, height: int):
        self.width = width - 1
        self.height = height - 1
        self.x = 0
        self.y = 0
        self.pos = 0
        self.length = 2 * (self.width + self.height)
        self.directions = {1:"East" , 2:"North" , 3:"West" , 4:"South"}
        self.direction = 1


    def step(self, num: int) -> None:
        mid_point = self.width + self.height

        self.pos = (self.pos + num) % self.length

        if (mid_point + self.width < self.pos < self.length or self.pos == 0):
            self.direction = 4
        elif (mid_point < self.pos <= mid_point + self.width):
            self.direction = 3
        elif (self.width < self.pos <= mid_point):
            self.direction = 2
        else:
            self.direction = 1

    def getPos(self) -> List[int]:
        mid_point = self.width + self.height

        if (mid_point + self.width < self.pos < self.length):
            relative_pos = self.pos - (mid_point + self.width)
            return [0 , self.height - relative_pos]

        elif (mid_point < self.pos <= mid_point + self.width):
            relative_pos = self.pos - mid_point
            return [self.width - relative_pos , self.height]

        elif (self.width < self.pos <= mid_point):
            relative_pos = self.pos - self.width
            return [self.width, relative_pos]
        else:
            return [self.pos ,0]


        

    def getDir(self) -> str:

        return self.directions[self.direction]



# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()