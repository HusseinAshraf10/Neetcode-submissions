class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l= 0
        max_seq= 0
        seen= set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+= 1
            seen.add(s[r])
            max_seq= max(max_seq, r - l + 1)
            
        return max_seq
