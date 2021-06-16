class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        head = 0
        tail = len(numbers)-1
                while head<tail:
            total = numbers[head] + numbers[tail]
            if target < total:
                tail-=1
            elif target > total:
                head+=1
            else:
                return [head+1, tail+1]
                            