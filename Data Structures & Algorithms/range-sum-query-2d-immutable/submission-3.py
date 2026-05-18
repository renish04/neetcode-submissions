class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        i = 0
        while i < len(self.matrix[0]):
            score = 0
            for j in range(len(self.matrix)):
                self.matrix[j][i] += score
                score = self.matrix[j][i]
            i += 1

        for i in range(len(self.matrix)):
            score = 0
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] += score
                score = self.matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        p = self.matrix[row2][col2]
        q = 0
        r = 0
        s = 0

        if row1 - 1 < 0:
            q = 0
        else:
            q = self.matrix[row1-1][col2]
        
        if col1 - 1 < 0:
            r = 0
        else:
            r = self.matrix[row2][col1-1]

        if row1 - 1  < 0 or col1 - 1 < 0:
            s = 0
        else:
            s = self.matrix[row1-1][col1-1]
        
        
        return  p - q - r + s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)