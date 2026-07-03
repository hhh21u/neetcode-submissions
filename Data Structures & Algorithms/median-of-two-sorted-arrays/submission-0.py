class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        half = total // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l, r = 0, len(nums1) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            l1 = nums1[i] if i >= 0 else -float("inf")
            r1 = nums1[i + 1] if i < len(nums1) - 1 else float("inf")

            l2 = nums2[j] if j >= 0 else -float("inf")
            r2 = nums2[j + 1] if j < len(nums2) - 1 else float("inf")

            if r2 >= l1 and r1 >= l2:
                if total % 2 == 1:
                    return min(r1, r2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif r2 < l1:
                r = i - 1
            else:
                l = i + 1
        