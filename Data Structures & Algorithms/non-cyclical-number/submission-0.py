class Solution:
    def calc(self,n):
        res = 0
        while n > 0:
            res += (n % 10) ** 2
            n //= 10
        return res

    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            n = self.calc(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
        return False
            

