class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l= 0
        max_window= 0
        count={}

        for r in range(len(s)):
            count[s[r]]= count.get(s[r], 0) + 1
            while (r-l+1) - max(count.values()) > k:
                count[s[l]]-= 1
                l+= 1
                
            max_window= max(max_window, r-l+1)
        return max_window
        