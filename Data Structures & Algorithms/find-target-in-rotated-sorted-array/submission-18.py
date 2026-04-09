class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) 
        if n == 0:
            return -1

        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            m = nums[mid]
            if m == target:
                return mid

            elif nums[l] <= m:
                if nums[l] <= target < m:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if m < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

