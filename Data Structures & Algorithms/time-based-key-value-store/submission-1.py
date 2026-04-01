class TimeMap:

    def __init__(self):
        self.store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store.get(key,[]) 
        if not pairs:
          return ""
        l,r=0,len(pairs)-1
        while l<=r:
            mid = (l+r)//2
            if pairs[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid -1
        if r >= 0:
            return pairs[r][1]
        else:
            return ""

