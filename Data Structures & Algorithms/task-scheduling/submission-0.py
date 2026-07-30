class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        pq = [] # (count) max heap by (-count)
        for key, num in count.items():
            heapq.heappush(pq, -num)
        q = deque([]) # (-count, timeline)
        time = 0
        while pq or q:
            time += 1
            if not pq:
                time = q[0][1] # new timeline
            else:
                n_cnt = 1 + heapq.heappop(pq)
                if n_cnt != 0:
                    q.append((n_cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(pq, q.popleft()[0])
        return time

