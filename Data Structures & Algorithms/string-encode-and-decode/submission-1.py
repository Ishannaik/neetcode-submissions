class Solution:
    

    def encode(self, strs: List[str]) -> str:
        lst = []
        new_str = ""
        for s in strs:
            new_str = new_str + str(len(s)) + "#" + s
        return new_str
    def decode(self, s: str) -> List[str]:
        hash_index = 0
        words = 0
        start = 0
        length = 0
        lst = []
        while hash_index < len(s):
            if s[hash_index] == "#":
               print(s[start:hash_index])
               length = int(s[start:hash_index])
               print("length:", length)
               print(s[hash_index+1: hash_index+1+length])
               lst.append(s[hash_index+1: hash_index+1+length])
               start = hash_index+1+length
               hash_index = hash_index+1+length
            hash_index +=1 
            print(hash_index)
        return lst
