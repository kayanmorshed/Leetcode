class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.row1, self.col1, self.row2, self.col2, self.newValue = row1, col1, row2, col2, newValue

        for i in range(self.row1, self.row2 + 1) :
            for j in range(self.col1, self.col2 + 1):
                self.rectangle[i][j] = self.newValue

    def getValue(self, row: int, col: int) -> int:
        self.row = row
        self.col = col
        return self.rectangle[self.row][self.col]



# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)