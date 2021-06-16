class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """        
        rows = len(matrix)
        if rows:
            columns = len(matrix[0])
                if rows == 0 or columns == 0 or matrix[0][0]> target:
            return False
                low, high = 0, rows*columns-1
                while low <= high:
            mid = low + (high-low)//2
            element = matrix[mid/columns][mid%columns]
            if element == target:
                return True
            elif element > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
                