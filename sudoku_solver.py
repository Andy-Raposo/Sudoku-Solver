puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

class Grid:
    
    def __init__(self):
        self.grid = grid
    # Initiates the grid within the class
    def find_empty_cell(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 0:
                    return (row, col)
        return None
    # This finds the empty cells in the board's grid, no matter the size (usually 9x9)

    def num_valid_in_row(self, row, num):
        if num not in self.grid[row]:
            return True
        return False
    # Checks the validity of the number in the row calling the grid

    def num_valid_in_col(self, col, num):
        for num in range(len(self.grid)):
            if self.grid[row][col] == num:
                return False
        return True
    # Checks the validity in the row, by measuring each num in "col" position within the rows
    
    def num_valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row in range(row_start, row_start + 3):
            for col in range (col_start, col_start + 3):
                if self.grid[row][col] == num:
                    return False
        return True
    
    
    def all_valid(self, row, col, num):
        num_valid_in_row = self.num_valid_in_row(row, num)
        num_valid_in_col = self.num_valid_in_col(col, num)
        num_valid_in_square = self.num_valid_in_square(row, col, num)
        # Simple call of all previous validation methods to return them
        return all([num_valid_in_row, num_valid_in_col, num_valid_in_square]) is True:
        # If all are true, then the number is valid to process in the solver
    
    def solution(self, guess, empty_cell):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True
        # Checks if the puzzle is complete once there are no more empty cells
        row, col = empty_cell
        for guess in range(1,10):
            if self.all_valid(row, col, num):
                self.grid[row][col] = num
                if self.solve():
                    return True
                self.grid[row][col] = 0
        return False
        # Core of the problem - guesses possible answers and backtracks if it finds a dead-end (unable to create a solution) until all the puzzle is complete. Since the range of answers goes from 0 to 8, there's a limited amount of iterations possible.