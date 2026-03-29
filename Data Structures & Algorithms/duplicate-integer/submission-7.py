class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet= set()
        for x in nums:
            if x in hashSet:
                return True
            hashSet.add(x)
        return False