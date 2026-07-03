class TimeMap:

    def __init__(self):
        self.timedict = defaultdict(list) # {Alice: (1, happy)}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timedict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timedict:
            return ""
        arr = self.timedict[key]
        l, r = 0, len(arr) - 1

        while l < r:
            mid = (l + r + 1) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            if arr[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid
        print(l)
        if arr[l][0] <= timestamp:
            return arr[l][1]
        else:
            return ""
