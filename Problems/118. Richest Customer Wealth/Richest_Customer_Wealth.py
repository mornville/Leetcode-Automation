class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        if len(accounts) == 0:
            return 0
        i = 0
        while i < len(accounts):
            sum = 0
            for j in range(0, len(accounts[0])):
                sum+=accounts[i][j]
            if sum > maxi:
                maxi = sum
            i+=1
        return maxi