class MedianFinder:

    def __init__(self):
        self.lst = []
        self.n = 0

    def addNum(self, num: int) -> None:
        self.lst.append(num)
        self.n += 1
        return None

    def findMedian(self) -> float:
        self.lst.sort()
        n = len(self.lst)
        if n == 0:
            return 0
        left = math.floor(n / 2)
        if n % 2 == 1:
            return round(self.lst[left], 1)
        else:
            return round((self.lst[left] + self.lst[left - 1]) / 2, 1)
        