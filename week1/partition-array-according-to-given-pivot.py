class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        equals = []
        greaters = []
        lessers = []
        for num in nums:
            if num > pivot:
                greaters.append(num)
            elif num < pivot:
                lessers.append(num)
            else:
                equals.append(num)
        return lessers + equals + greaters