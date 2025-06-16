# Last updated: 6/16/2025, 3:22:50 PM
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(1,numRows + 1):
            if i == 1:
                ret.append([1])
            elif i == 2:
                ret.append([1,1])
            else:
                row = [None] * i
                for j in range(i):
                    if j == 0 or j == i - 1:
                        row[j] = 1
                    else:
                        row[j] = ret[i - 2][j - 1] + ret[i - 2][j]
                ret.append(row)
        return ret
            
