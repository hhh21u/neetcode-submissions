class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 0 or len(trust) == 0:
            return -1
        trustL = [0] * (n + 1)
        isTrusted = [0] * (n + 1)

        for pair in trust:
            a, b = pair[0], pair[1]
            trustL[a] += 1
            isTrusted[b] += 1
        # print(trustL)
        # print(isTrusted)
        for i in range(1, n + 1):
            if trustL[i] == 0 and isTrusted[i] == n - 1:
                return i
        return -1