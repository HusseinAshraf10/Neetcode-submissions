class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        else:
            l, r = 1, max(piles)
            output = r
            
            while l <= r:
                k = l + (r - l) // 2
                hours = 0
                hours+= sum(math.ceil(pile / k) for pile in piles)
                
                if hours <= h:
                    output = k
                    r = k - 1
                else:
                    l = k + 1

            return output
