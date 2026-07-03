class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        def findMin():
            res, idx = nums[0], 0
            l, r = 0, len(nums) - 1
            while l <= r:
                if nums[l] < nums[r]:
                    if nums[l] < res:
                        res = nums[l]
                        idx = l
                    break
                mid = (l + r + 1) //2
                if nums[mid] < res:
                    res = nums[mid]
                    idx = mid
                if nums[mid] >= nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            return idx
        
        start = findMin()
        print(f"cur: {start}")

        def bin_search(arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r + 1) // 2
                if arr[mid] == target:
                    return mid
                if arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        
        left =  bin_search(nums[:start])
        right = bin_search(nums[start:])
        if left != -1: return left
        if right != -1: return right + start
        return -1
                