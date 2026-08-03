class Solution:
    def calc(self,n):
        res = 0
        while n > 0:
            res += (n % 10) ** 2
            n //= 10
        return res

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.calc(n)

        while slow != fast:
            slow = self.calc(slow)
            fast = self.calc(self.calc(fast))
        return True if fast == 1 else False
            

