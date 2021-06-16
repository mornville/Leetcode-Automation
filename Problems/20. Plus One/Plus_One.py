class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        maxLen = len(digits)-1
        ans = []
        carry = 0
        for i in range(0, len(digits)):
            if(i == 0):
                digit = digits[maxLen-i] + 1 + carry
            else:
                digit = digits[maxLen-i] + carry
            carry = 0
            if(digit>9):
                carry = 1
                digit = digit-10
            ans.append(digit)
            if(i==maxLen and carry == 1):
                ans.append(1)
        return [ele for ele in reversed(ans)]