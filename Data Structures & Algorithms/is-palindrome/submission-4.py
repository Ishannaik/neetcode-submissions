class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r = len(s)-1
        print(r)
        while l<r:
            while l<r:
                if not s[l].lower().isalnum():
                    l+=1
                else:
                    break
            while l<r:
                if not s[r].lower().isalnum():
                    r-=1
                else:
                    break
            if not s[l].lower() == s[r].lower():
                return False
            l+=1
            r-=1
        return True 

# What is the win condition?