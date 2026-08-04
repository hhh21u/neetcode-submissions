class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for num, f in count.items():
            freq[f].append(num)
        res = []
        for i in range(len(nums), -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res 