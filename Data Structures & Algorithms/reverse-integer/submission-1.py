class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31
        NEG_MAX = - 2 ** 31
        print(NEG_MAX)

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            print(res)
            if res > MAX // 10 or (res == MAX//10 and digit > MAX % 10):
                return 0
            if res < NEG_MAX // 10 or (res == NEG_MAX // 10 and digit < NEG_MAX % 10):
                return 0
            res = 10 * res + digit
        return res
