class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        def dfs(i):
            if i >= n - 1 or (i < n and nums[i] + i >= n - 1):
                return True
            rangei = nums[i]
            maxR, maxi = rangei, i
            for j in range(i + 1, min(n, i + rangei + 1)):
                # print(f"{nums[j]} + {j}, max:{maxR} + {maxi}")
                if nums[j] + j >= maxR + maxi:
                    print(f"f{j}")
                    maxR = nums[j]
                    maxi = j
            if maxi + maxR == i:
                return False
            # print(f"maxi: {maxi}")
            return dfs(maxi)

        return dfs(0)
            