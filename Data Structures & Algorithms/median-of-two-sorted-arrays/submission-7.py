class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        A, B = len(nums1), len(nums2)
        l, r = 0, A
        half = (A + B + 1) // 2
        
        while l <= r:
            i = (l + r) // 2
            j = half - i

            numsL1 = nums1[i - 1] if i > 0 else float("-inf")
            numsR1 = nums1[i] if i < A else float("inf")
            numsL2 = nums2[j - 1] if j > 0 else float("-inf")
            numsR2 = nums2[j] if j < B else float("inf")

            if numsL1 <= numsR2 and numsL2 <= numsR1:
                maxL = max(numsL1, numsL2)
                if (A + B) % 2:
                    return maxL
                return (maxL + min(numsR1, numsR2)) / 2
            elif numsL1 > numsR2:
                r = i - 1
            else:
                l = i + 1
        return 0.0