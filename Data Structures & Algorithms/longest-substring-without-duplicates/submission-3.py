class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_length = 0
        hashy = set()
        while r<len(s):
            if s[r] in hashy:
                hashy.remove(s[l])
                l += 1
            else:
                hashy.add(s[r])
                max_length = max(max_length, r-l+1)
                r += 1
        
        return max_length
            

        