# coding:utf-8
# time:20180711
# author:yang

# title:两数之和
# 题目描述：
# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length=len(nums)
        for item in range(length):
            another_value=target-nums[item]
            
            if another_value in nums:
                another_index=nums.index(another_value)
                if another_index!=item:
                    return [item,another_index]
        return None