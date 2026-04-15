class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        A, B = len(nums1), len(nums2)
        half = (A + B + 1) // 2
        l, r = 0, A
        while l <= r:
            i = (l + r) // 2
            j = half - i

            nL1 = nums1[i - 1] if i > 0 else float('-inf')
            nR1 = nums1[i] if i < A else float('inf')

            nL2 = nums2[j - 1] if j > 0 else float('-inf')
            nR2 = nums2[j] if j < B else float('inf')

            if nL1 <= nR2 and nL2 <= nR1:
                max_l = max(nL1, nL2)
                if (A + B) % 2:
                    return max_l
                return (max_l + min (nR1, nR2)) / 2
            elif nL1 > nR2:
                r = i - 1
            else:
                l = i + 1
        return 0.0
