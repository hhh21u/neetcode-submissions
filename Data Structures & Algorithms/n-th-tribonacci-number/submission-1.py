class Solution:
    def tribonacci(self, n: int) -> int:
        # if n == 
        arr = [0 for _ in range(max(3, n + 1))]
        arr[1] = arr[2] = 1
        for i in range(3, n + 1):
            arr[i] = arr[i - 3] + arr[i - 2] + arr[i - 1]
        return arr[n]