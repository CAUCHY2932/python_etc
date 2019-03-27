# coding:utf-8
# time:20180711
# author:yang

# title: 三数之和

# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        count = len(nums)
        collect = []
        for i in range(count):
            left = i+1
            right = count-1
            #避免重复找同一个数据
            if i >0 and nums[i] == nums[i-1]:
                left +=1
                continue
            #数据按小到大排列，每次选取nums[i]，在其后寻找符合a + b + c = 0的两个数据
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    col = [nums[i],nums[left],nums[right]]
                    collect.append(col)
                    left+=1
                    right-=1
                    #循环中nums[i]已确定，当再确定1个数时，另一个数也确定，左右端任一端出现重复均可跳过
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
                    while nums[right] == nums[right+1] and left < right:
                        right-=1
                if sum<0:
                    left+=1
                elif sum > 0:
                    right-=1
        return collect

# 作者：HBYeah
# 链接：https://www.jianshu.com/p/588caa7567c1
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。