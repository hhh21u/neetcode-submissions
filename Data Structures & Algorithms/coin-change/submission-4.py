class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        visited = {}
        def dp(remain, idx, steps):
            # print(f"enter{remain}, {idx}, {steps}")
            if remain == 0:
                return steps
            if idx < 0:
                return float("inf")
            if remain in visited and visited[remain] != float("inf"):
                # print(f"visited: {visited}")
                return visited[remain]
            # print(f" {remain}")
            count = remain // coins[idx]
            visited[remain] = float("inf")
            for i in range(count, -1, -1):
                # print(f"{coins[idx]}, {count}, {remain}")
                visited[remain] = min(visited[remain], 
                dp(remain - i * coins[idx], idx - 1, steps + i))
            return visited[remain]
        
        res = dp(amount, len(coins) - 1, 0) 
        return -1 if res == float("inf") else res
            
