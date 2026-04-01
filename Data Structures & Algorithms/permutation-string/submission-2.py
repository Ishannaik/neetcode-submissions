class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        l=0
        r=size-1
        map1={}
        map2={}
        for c in s1:
            map1[c] = map1.get(c,0) + 1
        for c in s2[:size]:
            map2[c] = map2.get(c, 0) + 1
        for i in range(len(s2)-size):
            if map1==map2:
                return True
            else:
                print(map1,map2)
                map2[s2[l]] -= 1
                map2[s2[r+1]] = map2.get(s2[r+1],0)+1
                if map2[s2[l]] == 0:
                    del map2[s2[l]]
                l+=1
                r+=1
        return map1 == map2



