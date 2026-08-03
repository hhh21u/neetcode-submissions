class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1: return x
        count = 1
        res = x
        if n == 0: return 1
        tune_n = n
        if n < 0: 
            tune_n = -n

        while count * 2 < tune_n:
            res = res * res
            count = 2 * count
        
        while count < tune_n:
            res *= x
            count += 1
        return res if n > 0 else 1 / res