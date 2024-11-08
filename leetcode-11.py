class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        maxArea = 0

        def calcArea(height, start, end):
            return min(height[start], height[end]) * (end - start)
        while start < end:
            area = calcArea(height, start, end)
            maxArea = max(area, maxArea)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maxArea
