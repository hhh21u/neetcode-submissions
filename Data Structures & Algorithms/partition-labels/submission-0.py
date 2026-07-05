class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        subCount = defaultdict(int)
        l = 0
        res = []
        prev = -1
        while l < len(s):
            cur = s[l]
            if cur not in subCount:
                subCount[cur] = count[cur] - 1
            else:
                subCount[cur] -= 1
            if subCount[cur] == 0:
                del subCount[cur]
            if len(subCount) == 0:
                res.append(l - prev)
                prev = l
            l += 1
        return res