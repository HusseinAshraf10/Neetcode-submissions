class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        # Step 1: Find the pivot (index of minimum element)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        min_i = l

        # Step 2: Decide which portion to search
        if nums[min_i] == target:
            return min_i

        # If target is in the left sorted portion
        if min_i > 0 and nums[0] <= target <= nums[min_i - 1]:
            l, r = 0, min_i - 1
        else:
            # Target is in the right sorted portion
            l, r = min_i, n - 1

        # Step 3: Normal binary search in the chosen portion
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1