class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # digits  [0] -> [1] [99] -> [100] [199] -> [200] [79] -> [80]

        n = len(digits)

        # iterate the arr reversely 
        # calculate any leftover

        # if need to add additional item -> dequ

        rem = 0
        last = digits[-1] + 1
        if last < 10:
            digits[-1] = last
            return digits
        else:
            rem = last // 10
            last %= 10
            digits[-1] = last
        for i in range(n - 2, -1, -1):
            val = digits[i] + rem
            if val >= 10:
                rem = val // 10
                val = val % 10
            else:
                rem = 0
            digits[i] = val
        if rem > 0:
            dq = deque(digits)
            dq.appendleft(rem)
            digits = list(dq)
        return digits