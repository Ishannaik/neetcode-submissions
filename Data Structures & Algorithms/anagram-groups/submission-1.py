class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            sortedS = "".join(sorted(str))
            res[sortedS].append(str)
        return list(res.values())