class Solution:
    """
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.


    """
    def runningSum(self, nums: List[int]) -> List[int]:
        lis = []
        lis.append(nums[0])
        for i in range(1,len(nums)):
            lis.append(lis[i-1] + nums[i])
        return lis