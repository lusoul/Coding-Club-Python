class TwoSumSolution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int] 返回下标
        """
        dic = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dic:
                return [dic[target - nums[i]], i]
            else:
                dic[nums[i]] = i