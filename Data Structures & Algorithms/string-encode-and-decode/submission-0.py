class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded = encoded + str(len(i)) + ":" + i
        return encoded
    def decode(self, s: str) -> List[str]:
        a=0
        decoded=[]
        while a < len(s):
            colon = s.find(':',a)
            length = int(s[a:colon])

            a = colon+ 1
            decoded.append(s[a:a+length]) 

            a=a+length
    
        return decoded

