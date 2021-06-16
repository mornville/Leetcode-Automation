class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for x in logs:
            if '../' in x:
                if count == 0 :
                    pass
                else:
                    count-=1
            elif './' in x:
                pass
            else:
                count+=1
                           return count