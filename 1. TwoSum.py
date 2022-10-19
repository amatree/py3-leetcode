class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for p in range(len(nums)):
            for i in range(p+1, len(nums)):
                if (nums[p] + nums[i] == target):
                    return [p, i]
                    