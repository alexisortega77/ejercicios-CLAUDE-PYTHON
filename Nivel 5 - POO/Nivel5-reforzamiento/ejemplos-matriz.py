class Matrix2x2:
    def __init__(self, data):
        self.data = data

    def get_element(self, row, col):
        return self.data[row][col]
    
    def set_element(self, row, col, value):
        self.data[row][col] = value

    def row_sum(self, row):
        return self.data[row][0] + self.data[row][1]
    
    def total_sum (self):
        return (
            self.data[0][0] +
            self.data[0][1] +
            self.data[1][0] +
            self.data[1][1] 
        )
    def column_sum(self,col):
        return (
            self.data[0][col]+self.data[1][col]
        )
    def max_value(self):
        return max(
            self.data[0][0],
            self.data[0][1],
            self.data[1][0],
            self.data[1][1],
        )
    def min_value(self):
        return min(
            self.data[0][0],
            self.data[0][1],
            self.data[1][0],
            self.data[1][1],
        )
    def swap_row(self):
       self.data[0],self.data[1] =self.data[1],self.data[0]
    def __str__(self):
        return f"{self.data[0]}\n{self.data[1]}"
        
m = Matrix2x2([[1,2],[3,4]])

print(m.get_element(0,1))   # 2

#m.set_element(1,0,10)


# [1, 2]
# [10, 4]


print(m.row_sum(0))   # 3
print(m.total_sum())  # 17       

print(m.column_sum(0) )#→ 4   # 1 + 3
print(m.max_value())
print(m.min_value())
m.swap_row()
print(m)