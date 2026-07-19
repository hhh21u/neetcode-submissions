from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        s1count, s2count = [0] * 26, [0] * 26
        for i in range(n1):
            pos1 = ord(s1[i]) - ord('a')
            pos2 = ord(s2[i]) - ord('a')
            s1count[pos1] += 1
            s2count[pos2] += 1
        matches = 0
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1
        l = 0 
        for r in range(n1, n2):
            if matches == 26:
                return True
            cur_r = ord(s2[r]) - ord('a')
            s2count[cur_r] += 1
            if s1count[cur_r] == s2count[cur_r]:
                matches += 1
            elif s1count[cur_r] == s2count[cur_r] - 1:
                matches -= 1

            prev_l = ord(s2[l]) - ord('a')
            s2count[prev_l] -= 1
            if s1count[prev_l] == s2count[prev_l]:
                matches += 1
            elif s1count[prev_l] == s2count[prev_l] + 1:
                matches -= 1
            l += 1

        return matches == 26
