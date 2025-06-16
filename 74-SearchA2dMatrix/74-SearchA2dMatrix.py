# Last updated: 6/16/2025, 3:22:55 PM
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        num_rows, num_cols = len(matrix), len(matrix[0])

        #find the row

        l, r = 0, num_rows - 1
        target_row = -1
        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                if (mid == num_rows - 1) or (mid < num_rows - 1 and matrix[mid + 1][0] > target): 
                    #found the target row
                    target_row = mid
                    break
                else:
                    l = mid + 1
            else: #matrix[mid][0] > target
                if (mid == 0):
                    return False
                else:
                    r = mid - 1
        if target_row == -1:
            return False



        row = matrix[target_row]
        left, right = 0, num_cols - 1

        while left <= right:
            middle = (left + right) // 2

            if row[middle] == target:
                return True
            elif row[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return False