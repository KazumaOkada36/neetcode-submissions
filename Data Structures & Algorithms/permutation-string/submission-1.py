class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashy = {}
        for letter in s1:
            if letter in hashy:
                hashy[letter] += 1
            else:
                hashy[letter] = 1
        lengthy = len(s1)
        l, r = 0, lengthy-1
        temp_hashy = {}
        while r<len(s2):
            for a in s2[l:r+1]:
                if a in temp_hashy:
                    temp_hashy[a] += 1
                else:
                    temp_hashy[a] = 1
            if temp_hashy == hashy:
                return True
            temp_hashy = {}
            r += 1
            l += 1
        

        return False

        