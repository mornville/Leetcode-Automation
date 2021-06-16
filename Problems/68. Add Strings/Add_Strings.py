class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        value = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        value2= {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
        print(value)
        result1 = 0
        result2 = 0
        for digit in num1:
            result1 = 10 * result1 + value[digit]
        for digit in num2:
            result2 = 10 * result2 + value[digit]
        result = result1 + result2
        print(result)
        finalAns = ""
        if(result==0):
            return "0"
        while(result>0):
            finalAns = value2[result%10] + finalAns
            result = result/10
        return finalAns