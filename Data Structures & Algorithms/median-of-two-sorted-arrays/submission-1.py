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

            L1 = nums1[i - 1] if i > 0 else float("-inf")
            R1 = nums1[i] if i < A else float("inf")
            L2 = nums2[j - 1] if j > 0 else float("-inf")
            R2 = nums2[j] if j < B else float("inf")

            if L1 <= R2 and L2 <= R1:
                max_l = max(L1, L2)
                if (A + B) % 2:
                    return max_l
                return (max_l + min(R1, R2)) / 2.0
            elif L1 > R2:
                r = i - 1
            else:
                l = i + 1
        return 0.0