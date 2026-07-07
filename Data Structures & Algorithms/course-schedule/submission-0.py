class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        req = [0] * numCourses
        prereq2course = defaultdict(list)
        for cur, requisite in prerequisites:
            req[cur] += 1
            prereq2course[requisite].append(cur)
        zeros = []
        for i in range(numCourses):
            if req[i] == 0:
                zeros.append(i)
        if len(zeros) == 0:
            return False
        
        while zeros:
            cur = zeros.pop()
            for nxt in prereq2course[cur]:
                req[nxt] -= 1
                if req[nxt] == 0:
                    zeros.append(nxt)
        return True if sum(req) == 0 else False