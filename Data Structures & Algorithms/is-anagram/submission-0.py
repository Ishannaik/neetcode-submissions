class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sfreq = {}
        tfreq = {}
        for ch in s:
            sfreq[ch] = sfreq.get(ch,0) + 1 
        for ch in t:
            tfreq[ch] = tfreq.get(ch,0) + 1     
        if sfreq == tfreq:
            return True
        else:
            return False