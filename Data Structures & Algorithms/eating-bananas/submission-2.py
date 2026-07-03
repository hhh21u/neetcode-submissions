class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if h < n: 
            return -1
        

        def countH(rate):
            res = 0
            for p in piles:
                res += math.ceil(p / rate)
            return res

        l, r = 1, max(piles)
        res = float("inf")
        while l <= r:
            mid = (l + r + 1) // 2
            count = countH(mid)
            if count <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
