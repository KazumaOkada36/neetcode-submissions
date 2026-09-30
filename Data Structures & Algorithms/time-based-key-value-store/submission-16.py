class TimeMap:

    def __init__(self):
        self.listy = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.listy:
            self.listy[key].append([timestamp, value])
        else:            
            self.listy[key] = [[timestamp, value]]
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.listy:
            return ""
        bruh = self.listy[key]
        l, r = 0, len(bruh)-1
        if bruh[0][0] > timestamp:
            return ""
        while l <= r:
            mid = (l+r)//2
            if bruh[mid][0] == timestamp:
                return bruh[mid][1]
            elif bruh[mid][0] > timestamp:
                r = mid-1
            elif bruh[mid][0] < timestamp:
                l = mid+1
        return bruh[r][1]
            
