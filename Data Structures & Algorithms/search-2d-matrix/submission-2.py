class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix) , len(matrix[0])
        topR, botR = 0, ROWS - 1

        while topR <= botR:
            row = (topR + botR) // 2
            if target > matrix[row][-1]:
                topR = row + 1
            elif target < matrix[row][0]:
                botR = row - 1
            else:
                break
        
        if not (topR <= botR):
            return False
        l, r = 0, COLS -1 
        while l <= r:
            mid = l + (r - l) //2

            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False

