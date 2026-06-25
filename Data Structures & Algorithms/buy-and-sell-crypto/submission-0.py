class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 100
        if not prices: return 0
        res = 0
        for p in prices:
            if p <= minPrice:
                minPrice = p
                continue
            res = max(res, p - minPrice)
        return res