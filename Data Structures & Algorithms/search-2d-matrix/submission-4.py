class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0 , ROWS * COLS - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target > matrix[mid // COLS][mid % COLS]:
                l = mid + 1
            elif target < matrix[mid // COLS][mid % COLS]:
                r = mid - 1
            else:
                return True
        return False