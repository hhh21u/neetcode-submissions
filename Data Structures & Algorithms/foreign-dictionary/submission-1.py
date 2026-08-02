class Node:
    def __init__(self, val = ""):
        self.val = val
        self.children = {} # dict started maintain order after 3.7
        self.startVal = None

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #topo

        indegree = {c: 0 for w in words for c in w}
        adjMap = defaultdict(set)

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w2) < len(w1) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adjMap[w1[j]]:
                        adjMap[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while q:
            lenq = len(q)
            for _ in range(lenq):
                c = q.popleft()
                res.append(c)
                for to in adjMap[c]:
                    indegree[to] -= 1
                    if indegree[to] == 0:
                        q.append(to)

        if len(res) != len(indegree):
            return ""
        return "".join(res)


