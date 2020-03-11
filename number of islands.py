"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input:
11110
11010
11000
00000
Output: 1

Time Complexity O(num_rows * num_columns)
Space Complexity O(num_rows * num_columns)
"""

def count_islands(matrix):
  count = 0
  for row in range(len(matrix)):
    for col in range(len(matrix[row])):
      if matrix[row][col] == '1':
        dfs(row, col, matrix)
        matrix[row][col] = None
        count += 1
  return count

def dfs(row, col, matrix):
  if row in range(len(matrix)) and col in range(len(matrix[row])) and matrix[row][col] == '1':
    matrix[row][col] = None
    dfs(row+1, col, matrix)
    dfs(row, col+1, matrix)
    dfs(row-1, col, matrix)
    dfs(row, col-1, matrix)
  
grid1 = [['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0']]
print(count_islands(grid1))

grid2 = [['1','1','0','0','0'],
         ['1','1','0','0','0'],
         ['0','0','1','0','0'],
         ['0','0','0','1','1']]
print(count_islands(grid2))
  
