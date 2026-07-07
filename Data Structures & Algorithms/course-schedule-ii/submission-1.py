class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        prereq2courses = defaultdict(list)

        for cur, pre in prerequisites:
            prereq2courses[pre].append(cur)
            indegree[cur] += 1
        
        q = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        res = []
        visited = set()
        while q:
            cur = q.popleft()
            if cur not in visited: 
                res.append(cur)
                visited.add(cur)
            for nxt in prereq2courses[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0 and nxt not in visited:
                    q.append(nxt)
        # print(res)
        return res if len(res) == numCourses else []