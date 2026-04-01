class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        length = 0
        l=0
        for r in range(len(s)):
            if not s[r] in hashset:
                hashset.add(s[r])
                print(hashset)
                length = max(len(hashset),length)
                print(length)
            else:
                while s[r] in hashset:
                    hashset.remove(s[l])
                    l+=1
                hashset.add(s[r])
        return length