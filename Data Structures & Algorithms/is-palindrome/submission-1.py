class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string="" #EMPTY STRING

        for b in s: #REMOVE NON WORD CHARACTERS + SMALL 
            if(b.isalnum()==True):
                new_string = new_string + b.lower()

        reverse_s = new_string[::-1]
        
        if (reverse_s==new_string):
            return True

        return False