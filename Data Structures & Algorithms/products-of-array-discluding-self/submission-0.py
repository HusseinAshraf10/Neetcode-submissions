class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)

        before=[0] * n 
        after=[0] * n
        total=[0] * n

        multi= 1 

        for x in range(n):
            before[x]= multi
            multi*= nums[x]

        multi= 1

        for x in range(n -1, -1, -1):
            after[x]=multi
            multi*=nums[x]

        for i in range(n):
            total[i]= before[i] * after[i]

        return total