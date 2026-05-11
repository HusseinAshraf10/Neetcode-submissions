class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]           # 1 step
            fast = nums[nums[fast]]     # 2 steps
            if slow == fast:
                break                   # they met inside the cycle

        # Phase 2: find cycle entry = duplicate
        slow = nums[0]                  # reset slow to start
        while slow != fast:
            slow = nums[slow]    
            fast = nums[fast]           

        return slow 
        
        
        
        
        
        
        # slow = nums[0]
        # fast = nums[0]

        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break
        # slow = nums[0]

        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[fast]
        # return slow