class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        countS1 = [0] * 26
        window = [0] * 26

        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord("a")] += 1
            window[ord(s2[i]) - ord("a")] += 1

        if countS1 == window: return True

        l= 0
        for r in range(len(s1), len(s2)):
            window[ord(s2[r]) - ord("a")] += 1
            window[ord(s2[l]) - ord("a")] -= 1
            l+= 1
            
            if window == countS1: return True

        else:
            return False
