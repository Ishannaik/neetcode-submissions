class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        lst = []
        final = []
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        print(freq)
        for key, value in freq.items():
            lst.append((value,key))
        lst = sorted(lst)[::-1]
        print(lst)
        for i in range(k):
            final.append(lst[i][1])
            print(final)
        return final