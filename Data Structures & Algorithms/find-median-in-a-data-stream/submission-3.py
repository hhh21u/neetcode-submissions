class MedianFinder:

    def __init__(self):
        self.pq = []
        self.n = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.pq, num)
        self.n += 1
        return None

    def findMedian(self) -> float:
        if self.n == 0:
            return 0
        right = math.floor(self.n / 2)
        left = right - 1
        q = []
        i = 0
        l_val = 0
        while i <= left:
            l_val = heapq.heappop(self.pq)
            q.append(l_val)
            i += 1
        r_val = heapq.heappop(self.pq)
        q.append(r_val)
        for val in q:
            heapq.heappush(self.pq, val)
        # print(f"{self.n}, {self.pq}, {left}, {right}")
        if self.n % 2 == 1:
            return r_val
        else:
            return round((l_val + r_val) / 2, 1)
        