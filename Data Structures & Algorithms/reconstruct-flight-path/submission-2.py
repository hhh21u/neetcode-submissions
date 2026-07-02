class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_map = defaultdict(list)

        for u, v in tickets:
            adj_map[u].append(v)
        for src in adj_map:
            adj_map[src].sort()
        visited = set()
        res = ["JFK"]
        def dfs(cur):
            if len(res) == len(tickets) + 1:
                return True
            if cur not in adj_map:
                return False
            tmp = adj_map[cur]
            for i, to in enumerate(tmp):
                adj_map[cur].pop(i)
                res.append(to)
                if dfs(to): 
                    return True
                adj_map[cur].insert(i, to)
                res.pop()
        dfs("JFK")
        return res


