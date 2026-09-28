class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for t in range(len(temperatures)):
            county = 0
            while stack and temperatures[stack[-1]] < temperatures[t]:
                a = stack.pop()
                county += 1
                result[a] = t-a
            stack.append(t)

        return result



        