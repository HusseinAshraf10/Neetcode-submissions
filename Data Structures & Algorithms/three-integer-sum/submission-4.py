class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        l= len(nums)

        for i in range(l - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left= i + 1
            right= l - 1
            while left < right:
                sum_nums= nums[i] + nums[left] + nums[right]

                if sum_nums == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left+= 1
                    right-= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left+= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right-= 1

                elif sum_nums < 0:
                    left+= 1
                else:
                    right-= 1

        return result
        
