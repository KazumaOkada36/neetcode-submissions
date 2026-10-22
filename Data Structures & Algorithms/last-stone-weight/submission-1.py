class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x = stones.pop()
            y = stones.pop()
            if x == y:
                continue
            elif x < y:
                a = y-x
                stones.append(a)
            elif y < x:
                a = x - y
                stones.append(a)           

        if len(stones) == 0:
            return 0
        else:
            return stones[0]
        