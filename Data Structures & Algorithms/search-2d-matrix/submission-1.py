class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        top, bot = 0, m - 1

        while top <= bot:
            mid_row = (top + bot) // 2
            if target>matrix[mid_row][-1]:
                top = mid_row +1
            elif target<matrix[mid_row][0]:
                bot = mid_row -1
            else:
                break

        l, r = 0, n - 1
        while l <= r:
            mid_col = (l + r) // 2
            if target>matrix[mid_row][mid_col]:
                l = mid_col + 1
            elif target<matrix[mid_row][mid_col]:
                r = mid_col - 1
            else:
                return True
        return False