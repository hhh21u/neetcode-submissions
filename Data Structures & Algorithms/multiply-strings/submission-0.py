class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1, len2 = len(num1), len(num2)
        if num1 == "0" or num2 == "0": return "0"

        if len1 > len2:
            num1, num2 = num2, num1
            len1, len2 = len2, len1
        # this ensures num1 is always having less item
        res = ""
        multi = 1
        total = 0
        for i in range(len1 - 1, -1, -1):
            n1 = int(num1[i])
            val = 0
            rem = 0
            muti_2 = multi
            for j in range(len2 - 1, -1, -1):
                n2 = int(num2[j])
                prod = n1 * n2 + rem
                val += (prod % 10) * muti_2
                rem = prod // 10
                muti_2 *= 10
            val += rem * muti_2
            total += val
            multi = multi * 10
        res = ""
        while total:
            res = str(total % 10) + res
            total //= 10
        return res
            
