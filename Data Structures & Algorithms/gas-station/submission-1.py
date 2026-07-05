class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        remain = []
        starts = []
        for i in range(n):
            dif = gas[i] - cost[i]
            remain.append(dif)
            if dif >= 0:
                starts.append(i)
        
        for start in starts:
            sub = 0
            for i in range(start, start + n):
                sub += remain[i % n]
                # print(f"{remain}, {sub}")
                if sub < 0: break
            if sub >= 0: return start
        return -1
