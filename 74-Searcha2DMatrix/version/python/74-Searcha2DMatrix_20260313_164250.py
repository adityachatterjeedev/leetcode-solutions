# Last updated: 3/13/2026, 4:42:50 PM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        
4        #find the correct row
5
6        l, r = 0, len(matrix) - 1
7
8        row_num = 0
9
10        while l <= r:
11            mid = (l + r) // 2
12            row_start = matrix[mid][0]
13            if row_start == target:
14                return True
15            elif row_start > target:
16                r = mid - 1
17            else:
18                row_num = mid
19                l = mid + 1
20        
21        #search in row_num
22        l, r = 0, len(matrix[row_num]) - 1
23
24        while l <= r:
25            mid = (l + r) // 2
26            if matrix[row_num][mid] == target:
27                return True
28            elif matrix[row_num][mid] > target:
29                r = mid - 1
30            else:
31                l = mid + 1
32
33        return False
34