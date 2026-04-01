class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                j, h = stack.pop()
                max_area = max(max_area, h * (i - j))
                start = j
            stack.append((start, height))

        while stack:
            j, h = stack.pop()
            max_area = max(max_area, h * (len(heights) - j))
        return max_area