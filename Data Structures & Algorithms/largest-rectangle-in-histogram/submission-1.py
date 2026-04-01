class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                j, h = stack.pop()
                w = i - j
                max_area = max(max_area, h * w)
                start = j
            stack.append((start, height))

        while stack:
            j, h = stack.pop()
            w = len(heights) - j
            max_area = max(max_area, h * w)
        return max_area