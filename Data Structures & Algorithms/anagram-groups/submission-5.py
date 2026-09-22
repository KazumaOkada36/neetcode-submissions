class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bighashy = {}
        for word in strs:
            hashy =[0] * 26
            for letter in word:
                hashy[ord(letter)-ord('a')] += 1
            hashy = tuple(hashy)
            if hashy in bighashy:
                bighashy[hashy].append(word)
            else:
                bighashy[hashy] = [word]
        result = []
        for i in bighashy.values():
            result.append(i)
        return result
