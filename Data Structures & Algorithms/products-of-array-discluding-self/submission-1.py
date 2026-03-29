class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        res=[1] * n

        prefix= 1
        for x in range(n):
            res[x]= prefix
            prefix*= nums[x]

        suffix= 1
        for x in range(n -1, -1, -1):
            res[x]*= suffix
            suffix*= nums[x]
        return res