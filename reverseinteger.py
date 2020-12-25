class Solution:
    """
    Given a 32-bit signed integer, reverse digits of an integer.
    Note:
    Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
    For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
    """
    def reverse(self, x: int) -> int:

        num = ""
        if str(x)[0] == '-':
            num = "-"+str(x)[:0:-1]
        else:
            num = str(x)[::-1]

        if (int(num) > -2**31) and (int(num) < ((2**31)-1)):
            return int(num)
        else:
            return 0