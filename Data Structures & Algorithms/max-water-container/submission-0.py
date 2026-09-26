class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        while l<r:
            heighty = min(heights[l], heights[r])
            area = heighty * (r-l)
            if heights[l]< heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r -= 1
            maxArea = max(area, maxArea)


        return maxArea
