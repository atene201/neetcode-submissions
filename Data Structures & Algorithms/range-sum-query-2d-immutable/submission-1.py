class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total_sum = 0
        range_row = row2 - row1 + 1
        range_col = col2 - col1 + 1
        for i in range(range_row * range_col):
            row = row1 + (i // range_col)
            col = col1 + (i % range_col)
            total_sum += self.matrix[row][col]
        
        return total_sum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)