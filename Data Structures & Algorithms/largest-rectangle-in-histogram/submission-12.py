class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:    
        maxArea = 0
        stack = []

        for i, height in enumerate(heights):
            indexy = i
            while stack and stack[-1][1] > height:
                indexy, heighty = stack.pop()
                Area = heighty * (i-indexy)
                maxArea = max(maxArea, Area)
            stack.append([indexy, height])
        

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights)-i))

        return maxArea

