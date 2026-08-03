class CountSquares:

    def __init__(self):
        self.row2cols = defaultdict(list)
        self.point2count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        r, c = point[0], point[1]
        self.point2count[(r, c)] += 1
        self.row2cols[r].append(c)

    def count(self, point: List[int]) -> int:
        r, c = point[0], point[1]
        count = 0
        for pc in self.row2cols[r]:
            if pc == c:
                continue
            dif = abs(c - pc)
            l1, l2, r1, r2 = None, None, (r + dif, c), (r - dif, c)
            if pc < c:
                l1 = (r + dif, c - dif)
                l2 = (r - dif, c - dif)
            else:
                l1 = (r + dif, c + dif)
                l2 = (r - dif, c + dif)
            if l1 in self.point2count and r1 in self.point2count:
                count += self.point2count[l1] * self.point2count[r1]
            if l2 in self.point2count and r2 in self.point2count:
                count += self.point2count[l2]* self.point2count[r2]
        return count
