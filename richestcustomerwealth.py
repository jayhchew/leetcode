class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        account = 0
        richest = 0
        for i in range(len(accounts)):
            if (account > richest):
                richest = account
            account = 0
            for j in range(len(accounts[i])):
                account += accounts[i][j]
            if (len(accounts) == 1):
                richest = account

        return richest