class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dis = [float("inf") for _ in range(n)]
        
        dis[src] = 0

        for _ in range(k + 1): # 0 
            temp_dis = dis.copy()
            for u, v, w in flights:
                if dis[u] != float("inf") and dis[u] + w < temp_dis[v]: 
                    temp_dis[v] = dis[u] + w
            dis = temp_dis
        
        return dis[dst] if dis[dst] != float("inf") else -1
                
