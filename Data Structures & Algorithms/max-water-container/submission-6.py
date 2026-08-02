class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area, current_area = 0, 0
        while left < right:
            current_area = (right - left) * min(heights[left], heights[right])
            if current_area > max_area:
                max_area = current_area
            if (heights[left] > heights[right]):
                right -= 1
            elif (heights[right] > heights[left]):
                left += 1
            else:
                left += 1
                right -= 1
        return max_area
