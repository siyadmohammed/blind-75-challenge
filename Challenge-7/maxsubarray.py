class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsubarr = nums[0]
        carrsum = 0
        for n in nums:
            if carrsum < 0:
                carrsum = 0
            carrsum += n
            maxsubarr = max(maxsubarr , carrsum) 
        return maxsubarr