# 23. Search a 2D Matrix
### Difficulty: Medium
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties: <br/> Integers in each row are sorted from left to right. <br/> The first integer of each row is greater than the last integer of the previous row. <br/>   <br/><b>- Example</b> 1: <br/> Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 <br/> Output: true <br/> <br/><b>- Example</b> 2: <br/> Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13 <br/> Output: false <br/>   Constraints: <br/> m == matrix.length <br/> n == matrix[i].length <br/> 1 <= m, n <= 100 <br/> -104 <= matrix[i][j], target <= 104