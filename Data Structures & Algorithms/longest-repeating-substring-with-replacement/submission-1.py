class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l= 0
        max_win= 0
        count={}
        
        for r in range(len(s)):
            count[s[r]]= count.get(s[r], 0) + 1

            if (r - l + 1) - max(count.values()) <= k:
                max_win= max(max_win, r - l + 1)
            else:
                count[s[l]]-= 1
                l+= 1
        return max_win