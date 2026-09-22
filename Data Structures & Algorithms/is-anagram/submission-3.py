class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashy1 = [0] * 27
        hashy2 = [0] * 27
        for letter in s:
            hashy1[ord(letter)-97] += 1
        for letter in t:
            hashy2[ord(letter)-97]+= 1
        if hashy1 == hashy2:
            return True
        return False
