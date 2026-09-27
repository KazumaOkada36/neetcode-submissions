class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        hashy = {}
        maximum_length = 0
        while r < len(s):
            if s[r] in hashy:
                hashy[s[r]] += 1
            else:
                hashy[s[r]] = 1
            maxy = max(hashy.values())
            replacements_needed = (r-l+1) - maxy
            while replacements_needed > k:
                hashy[s[l]] -= 1
                l += 1
                replacements_needed -= 1
            maximum_length = max(maximum_length, r-l+1)
            r += 1
        
        return maximum_length