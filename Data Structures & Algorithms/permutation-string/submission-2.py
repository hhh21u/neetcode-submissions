from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        count1 = Counter(s1)
        l = 0 
        def counterEqual(c1, c2):
            if len(c1) != len(c2):
                return False
            for key, val in c1.items():
                if key not in c2 or c2[key] != val:
                    return False
            return True

        for r in range(n1, n2 + 1):
            # print(f"sub: {s2[l:r]}")
            count2 = Counter(s2[l:r])
            if count1 == count2:
                return True
            l += 1
        return False
