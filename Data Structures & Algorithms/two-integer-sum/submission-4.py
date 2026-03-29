class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nput: nums = [4,5,6], target = 10
        #Output: [0,2]

        hashmap={}

        for i, x in enumerate(nums):
            needed = target - x
            if needed in hashmap:
                return [hashmap[needed], i]

            hashmap[x] = i

