class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * (cols + 1) for _ in range(rows + 1)] # make the sum_matrix 1-indexed

        for r in range(rows):
            prefix = 0 # calc the prefix for each idx
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.sum_matrix[r][c+1] # r doesn't get added 1 b/c of 1-indexed sum_matrix
                self.sum_matrix[r + 1][c + 1] += prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2, c1, c2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1 # easier to handle in sum_matrix

        btm_right = self.sum_matrix[r2][c2]
        top_left = self.sum_matrix[r1-1][c1-1]
        above = self.sum_matrix[r1-1][c2]
        left = self.sum_matrix[r2][c1-1]

        return btm_right - above - left + top_left # add top_left b/c it got subtracted twice (above, left)





# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)