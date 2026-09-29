class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:    
        if len(heights) == 0:
            return 0
        max_area = 0
        stacky = []
        for i, height in enumerate(heights):
            start = i
            while stacky and stacky[-1][1] > height:
                index, old_height = stacky.pop()
                width = i-index
                area = width * old_height
                max_area = max(max_area, area)
                start = index
            stacky.append([start, height])

        for index, height in stacky:
            width = len(heights) - index
            area = height * width
            max_area = max(max_area, area)
        return max_area
