from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        count1 = Counter(s1)
        l = 0 
        for r in range(n1, n2 + 1):
            count2 = Counter(s2[l:r])
            if count1 == count2:
                return True
            l += 1
        return False
