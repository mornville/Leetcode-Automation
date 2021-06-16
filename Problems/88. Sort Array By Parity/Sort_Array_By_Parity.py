class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        p1 = 0
        p2 = 0
        while p2<len(A):
            if A[p2] % 2 == 0:
                print('even')
                temp = A[p2]
                A[p2] = A[p1]
                A[p1] = temp
                p1+=1
            p2+=1
        return A