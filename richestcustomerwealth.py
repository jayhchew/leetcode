class Solution:
    """
    You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the jth bank. Return the wealth that the richest customer has.

    A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.


    """
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