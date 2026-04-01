class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        mapT = {}
        window = {}
        l,r=0,1
        have=0
        lowest=float("inf")
        for c in t:
            mapT[c] = mapT.get(c,0)+1
        print(mapT)
        need = len(mapT)
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in mapT and window[s[r]] == mapT[s[r]]:
                have+=1
            while have == need:
                if (r - l + 1) < lowest:
                    lowest = r - l + 1
                    start = l
                window[s[l]] -= 1
                if s[l] in mapT and window[s[l]] < mapT[s[l]]:
                    have -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
        return s[start:start+lowest] if lowest != float("inf") else ""

                



