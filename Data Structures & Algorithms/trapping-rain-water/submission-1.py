class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r= 0, len(height) -1 
        Max_left, Max_right= height[l], height[r]
        result= 0

        while l < r:
            if Max_left <= Max_right:
                l+= 1
                Max_left= max(Max_left, height[l])
                result+= Max_left - height[l]

            else:
                r-= 1
                Max_right= max(Max_right, height[r])
                result+= Max_right - height[r]

        return result