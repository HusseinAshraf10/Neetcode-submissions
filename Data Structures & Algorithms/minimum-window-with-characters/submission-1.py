class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window= {}, {}
        min_window, result= float("inf"), [-1, -1]

        for c in t:
            countT[c]= countT.get(c, 0) + 1

        have, need= 0, len(countT)
        
        l= 0 
        for r in range(len(s)):
            c= s[r]
            window[c]= window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have+= 1
            
            while have == need:
                if r - l + 1 < min_window:
                    min_window = r-l + 1
                    result = [l, r]
                
                window[s[l]]-= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-= 1
                l+= 1
        l, r= result
        return s[l: r + 1] if min_window != float("inf") else ""

                



                


