class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        if len(s) == 0:
            return res
        for i in range(len(s)):
            l, r = i, i
            while l>= 0 and r<len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            j, k = i, i+1
            while j>= 0 and k<len(s) and s[j] == s[k]:
                res += 1
                j -= 1
                k += 1
        
        return res
        