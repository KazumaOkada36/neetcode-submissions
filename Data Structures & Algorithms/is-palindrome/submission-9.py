class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<=j:
            if s[i] in [" ",".","?", ",", "'", ":", "!"]:
                i += 1
            elif s[j] in [" ",".","?", ",", "'", ":", "!"]:
                j -= 1
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        
        return True
