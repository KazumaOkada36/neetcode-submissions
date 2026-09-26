class Solution:
    def trap(self, height: List[int]) -> int:
        water_trapped = 0
        l, r = 0, len(height)-1
        leftmax = 0
        rightmax = 0
        while l<r:
            leftmax = max(leftmax, height[l])
            rightmax = max(rightmax, height[r])
            heighty = min(leftmax, rightmax)
            if height[l] < height[r]:
                water_trapped += heighty - height[l]
                l += 1
            elif height[r] < height[l]:
                water_trapped += heighty - height[r]
                r -= 1
            else:
                water_trapped += heighty - height[r]
                r -= 1

        return water_trapped
       