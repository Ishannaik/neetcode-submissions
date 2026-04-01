class Solution:
    def isPalindrome(self, s: str) -> bool:
        b=s
        newstr = ""
        for c in s:
            if c.isalnum():
                newstr += c.lower()

        print(b.lower())
        if newstr.lower() == newstr[::-1].lower():
            return True
        else:
            return False
        