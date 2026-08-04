class Solution:
    ### quickselect
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # element mapping to frequency
        uniqueIds = list(count.keys())

        # partition
        def partition(arr, l, r):
            pivot_freq = count[arr[r]]
            i = l
            for j in range(l, r):
                if count[arr[j]] <= pivot_freq:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[r], arr[i] = arr[i], arr[r]
            return i
        
        l, r = 0, len(uniqueIds) - 1
        # ascending order 1234> target k largest will be n-k smallest
        target = len(uniqueIds) - k
        while l <= r:
            p = partition(uniqueIds, l, r)
            if p == target:
                break
            elif p < target: 
                l = p + 1
            else:
                r = p - 1
        return uniqueIds[target:]

