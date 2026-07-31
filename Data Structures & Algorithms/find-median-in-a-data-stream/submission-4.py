class MedianFinder:

    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, - num)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            small_max = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, - small_max)
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            large_min = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, - large_min)
    

    def findMedian(self) -> float:
        n = len(self.maxHeap) + len(self.minHeap)
        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2.0
            
        
        