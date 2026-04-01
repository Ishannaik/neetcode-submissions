class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        lst = []
        freq = {}
        print(strs)
        for i in strs:
            key = ("".join(sorted(i)))
            if key not in freq:
                freq[key] = [i]
            else:
                freq[key].append(i)
        lst = list(freq.values())
        print(freq)
        return lst