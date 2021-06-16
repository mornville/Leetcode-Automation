class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        i = 0
        while i <= len(arr)-1:
            prod = arr[i:i+m]
            if prod * k == arr[i:i+m*k]:
                return True
            i += 1
        return False
                            