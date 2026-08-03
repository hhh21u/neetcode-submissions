from bisect import bisect_left
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # use binary search to find the pos of x
        # from that index, we can l, r pointers compare the left item distnace with the right item
        # if the left <= right, add to result - if the result len is == k > return res

        # edge case:
        if k == len(arr): #[-1000] x -> [-1000]
            return arr
    
        # [2, 4, 5, 8] # x-> 10
        n = len(arr) # 4
        l, r = 0, n - 1 # 0, 3
        res = []

        while (r - l + 1) > k: # 4 > 2 # 3 > 2
            dif_l, dif_r = abs(arr[l] - x), abs(arr[r] - x) # 4, 2 # 2 2
            if (dif_l <= dif_r):
                r -= 1 # 3 -> 2
            else:
                l += 1 # 0-> 1
            
        return arr[l:r + 1] #arrr[1: 3] -> [4, 5]



