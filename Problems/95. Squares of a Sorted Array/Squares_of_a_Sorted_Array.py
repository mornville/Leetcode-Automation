class Solution(object):
    def sortedSquares(self, A):
        n = len(A)
        positive = 0
        while positive < n and A[positive] < 0:
            positive += 1
        negative = positive - 1
        ans = []
        while 0 <= negative and positive < n:
            if A[negative]**2 < A[positive]**2:
                ans.append(A[negative]**2)
                negative -= 1
            else:
                ans.append(A[positive]**2)
                positive += 1
        while negative >= 0:
            ans.append(A[negative]**2)
            negative-= 1
        while positive < n:
            ans.append(A[positive]**2)
            positive += 1
        return ans
        """ One line solution"""
        # return sorted(num*num for num in A) 